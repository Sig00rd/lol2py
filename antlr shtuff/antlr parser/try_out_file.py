from antlr4 import *
from lolcodeParser import lolcodeParser
from lolcodeLexer import lolcodeLexer
from lolcodeListener import lolcodeListener


class lolcodePrintListener(lolcodeListener):
    def enterHi(self, ctx):
        print("Hello %s!" % ctx.ID())


def main():
    lexer = lolcodeLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = lolcodeParser(stream)
    tree = parser.hi()
    printer = lolcodePrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


if __name__ == '__main__':
    main()

# A (hopefully) helpful note regarding antlr
# so, it can be used with pycharm, you just have to install the antlr jetbrains plugin
# I've had some weird errors when I tried to install it normally, so I've installed an older version,
# upgraded it in pycharm to the newest and it seems to be working just fine now
# I've generated a lexer and a parser from our sample grammar, apparently you can't use rules that sound exactly
# like Python's, so our not just became a nope
# Also, this file is a sample start-up class. We'll also have to create a custom listener/visitor (I've experimented
# with a listener for now, I just don't really get the context variable yet)
# I think we'd have to write our python translation to another file and then execute that file to get the right effect
# we might also have to change our project's name from compiler to interpreter
