#include "scanner.h"

#include <cstdio>
#include <filesystem>
#include <vector>

static unsigned int GetTokenLength(const Scanner::ParserState &state)
{
	switch(state.token)
	{
		case TK_Identifier:
			return state.str.length();
		case TK_StringConst:
			return state.str.length()+2;
		case TK_IntConst:
		case TK_FloatConst:
			return 0; // Unsupported, not needed
		case TK_BoolConst:
			return state.boolean ? 4 : 5;
		case TK_AndAnd:
		case TK_OrOr:
		case TK_EqEq:
		case TK_NotEq:
		case TK_GtrEq:
		case TK_LessEq:
		case TK_ShiftLeft:
		case TK_ShiftRight:
		case TK_Increment:
		case TK_Decrement:
		case TK_PointerMember:
		case TK_ScopeResolution:
		case TK_MacroConcat:
		case TK_AddEq:
		case TK_SubEq:
		case TK_MulEq:
		case TK_DivEq:
		case TK_ModEq:
		case TK_AndEq:
		case TK_OrEq:
		case TK_XorEq:
			return 2;
		case TK_ShiftLeftEq:
		case TK_ShiftRightEq:
		case TK_Ellipsis:
			return 3;
		default:
			return 1;
	}
}

struct Xref
{
	enum Type
	{
		XT_ActorName,
		XT_Property,
		XT_Flag,
		XT_Function
	};

	Xref(const Scanner &sc, unsigned int relative, Type type) : start {sc->scanPos - GetTokenLength(*sc) - relative}, end {sc->scanPos - relative}, type {type}
	{
	}

	unsigned int start;
	unsigned int end;
	Type type;
};

struct Actor
{
	std::string name;
	std::string parent = "Actor";
	std::string definition;
	std::vector<Xref> xrefs;
};

std::vector<Actor> actorList;

static std::string ReadFileToString(const std::filesystem::path &filename)
{
	auto f = fopen(filename.c_str(), "rb");
	fseek(f, 0, SEEK_END);
	auto size = ftell(f);
	fseek(f, 0, SEEK_SET);

	std::vector<char> buffer;
	buffer.resize(size);

	fread(buffer.data(), size, 1, f);

	fclose(f);

	return {buffer.data(), size_t(size)};
}

static void ParseSkip(Scanner &sc)
{
	while(sc.GetNextToken())
	{
		if(sc->token == ';')
			break;

		if(sc->token == '{')
		{
			int level = 1;
			while(sc.GetNextToken())
			{
				if(sc->token == '}')
				{
					if(--level == 0)
						break;
				}
				else if(sc->token == '{')
				{
					++level;
				}
			}
			break;
		}
	}
}

static void ParseActorStates(Scanner &sc, unsigned int xrefRelative, Actor &actor)
{
	sc.MustGetToken('{');
	bool functionEligible = false;
	while(sc.GetNextToken() && sc->token != '}')
	{
		if(!functionEligible)
		{
			if(sc->token == TK_IntConst || sc->token == TK_FloatConst)
				functionEligible = true;
		}
		else
		{
			if(sc->token == TK_Identifier)
			{
				Xref xref {sc, xrefRelative, Xref::XT_Function};
				bool notFunction = (sc->str == "bright" || sc->str == "NOP" || sc->str == "offset");

				if(sc->str.length() == 4 || sc.CheckToken(':'))
				{
					functionEligible = false;
					continue;
				}

				if(sc.CheckToken('('))
				{
					int level = 1;
					while(sc.GetNextToken())
					{
						if(sc->token == ')')
						{
							if(--level == 0)
								break;
						}
						else if(sc->token == '(')
						{
							++level;
						}
					}
				}

				if(!notFunction)
					actor.xrefs.push_back(xref);
			}
			else
			{
				functionEligible = false;
			}
		}
	}
}

static Actor ParseActor(Scanner &sc, unsigned int xrefRelative)
{
	Actor actor;

	sc.MustGetToken(TK_Identifier);
	actor.name = sc->str;
	actor.xrefs.emplace_back(sc, xrefRelative, Xref::XT_ActorName);

	if(sc.CheckToken(':'))
	{
		sc.MustGetToken(TK_Identifier);
		actor.parent = sc->str;
		actor.xrefs.emplace_back(sc, xrefRelative, Xref::XT_ActorName);
	}

	while(sc.GetNextToken() && sc->token != '{');

	while(!sc.CheckToken('}'))
	{
		bool isFlag = false;
		if(sc.CheckToken('+') || sc.CheckToken('-'))
			isFlag = true;

		sc.MustGetToken(TK_Identifier);
		if(!isFlag && (sc->str == "states" || sc->str == "action" || sc->str == "native"))
		{
			if(sc->str == "states")
			{
				ParseActorStates(sc, xrefRelative, actor);
			}
			else if(sc->str == "action")
			{
				sc.MustGetToken(TK_Identifier);
				sc.MustGetToken(TK_Identifier);
				actor.xrefs.emplace_back(sc, xrefRelative, Xref::XT_Function);
				ParseSkip(sc);
			}
			else
			{
				ParseSkip(sc);
			}
		}
		else
		{
			Xref xref {sc, xrefRelative, isFlag ? Xref::XT_Flag : Xref::XT_Property};

			if(sc.CheckToken('.'))
			{
				sc.MustGetToken(TK_Identifier);
				Xref xref2 {sc, xrefRelative, xref.type};
				xref.end = xref2.end;
			}

			actor.xrefs.push_back(xref);

			if(!isFlag)
				sc.SkipLine();
		}
	}

	return actor;
}

static void XrefColorize(std::string &def, const std::vector<Xref> &xrefs)
{
	for(auto iter = xrefs.rbegin(); iter != xrefs.rend(); ++iter)
	{
		std::string colorCode;
		switch(iter->type)
		{
			case Xref::XT_ActorName:
				colorCode = "\e[1;32m";
				break;
			case Xref::XT_Property:
				colorCode = "\e[1;35m";
				break;
			case Xref::XT_Flag:
				colorCode = "\e[1;31m";
				break;
			case Xref::XT_Function:
				colorCode = "\e[1;34m";
				break;
		}

		def.insert(iter->end, "\e[0m");
		def.insert(iter->start, colorCode);
	}
}

static void PrintActor(const Actor& actor)
{
	printf("Code for %s:\n", actor.name.c_str());

	auto def = actor.definition;
	XrefColorize(def, actor.xrefs);
	printf("%s\n", def.c_str());
}

static void ParseFile(const std::filesystem::path &filename)
{
	printf("Parsing %s\n", filename.c_str());
	auto data = ReadFileToString(filename);

	Scanner sc {data.data(), data.size()};
	sc.SetScriptIdentifier(filename);

	while(sc.TokensLeft())
	{
		if(sc.CheckToken('#'))
		{
			sc.MustGetToken(TK_Identifier);
			if(sc->str == "include")
			{
				sc.MustGetToken(TK_StringConst);
				ParseFile(filename.parent_path() / sc->str);
			}
			else
				sc.SkipLine();
		}
		else
		{
			const auto entryStart = sc->scanPos;
			sc.MustGetToken(TK_Identifier);

			if(sc->str == "const")
			{
				ParseSkip(sc);
			}
			else if(sc->str == "actor")
			{
				auto actor = ParseActor(sc, entryStart);

				const auto entryEnd = sc->scanPos;
				actor.definition = data.substr(entryStart, entryEnd-entryStart);

				PrintActor(actor);
				actorList.push_back(actor);
			}
		}
	}
}

int main(int argc, char* argv[])
{
	ParseFile(argv[1]);
	return 0;
}
