import sys

from antlr4 import *
from antlr.lolcodeParser import lolcodeParser
from antlr.lolcodeLexer import lolcodeLexer
from antlr.lolcodeListener import lolcodeListener
from antlr.lolcodeCustomListener import lolcodeCustomListener


def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
    self.output.write(msg)
    self._symbol = offendingSymbol.text


def main():
    input = FileStream("example/input_file2.txt")
    lexer = lolcodeLexer(input)
    stream = CommonTokenStream(lexer)
    parser = lolcodeParser(stream)
    tree = parser.program()

    lolcodeChat = lolcodeCustomListener("output.py")
    walker = ParseTreeWalker()
    walker.walk(lolcodeChat, tree)


main()
