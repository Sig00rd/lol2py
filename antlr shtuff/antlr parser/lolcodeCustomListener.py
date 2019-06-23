from antlr4 import *
from .lolcodeParser import lolcodeParser
from .lolcodeLexer import lolcodeLexer
from .lolcodeListener import lolcodeListener
import re


# a good idea would probably be to try and implement the printing well

class lolcodeCustomListener(lolcodeListener):
    help_list = []
    loop_stack = []

    def enterHi(self, ctx):
        print("Hello %s!" % ctx.ID())

    def __init__(self, output):
        self.output = output

        # Enter a parse tree produced by lolcodeParser#program.

    def enterProgram(self, ctx: lolcodeParser.ProgramContext):
        pass

        # Exit a parse tree produced by lolcodeParser#program.

    def exitProgram(self, ctx: lolcodeParser.ProgramContext):
        # for i in range(1, len(self.help_list) - 1):
        #    if self.help_list[i] in ["elif ", "else "]:
        #        self.help_list.insert(i - 1, "")
        #        del self.my_list[i]
        index = 0
        to_save = []
        while index < len(self.help_list):
            to_save.append(self.help_list[index])
            index += 1
        for symbol in to_save:
            print(symbol, end="")
        with open('python_out.txt', 'w') as f:
            for item in self.help_list:
                f.write("%s" % item)
        pass

    # Enter a parse tree produced by lolcodeParser#code_block.
    def enterCode_block(self, ctx: lolcodeParser.Code_blockContext):
        pass

    # Exit a parse tree produced by lolcodeParser#code_block.
    def exitCode_block(self, ctx: lolcodeParser.Code_blockContext):
        pass

    # Enter a parse tree produced by lolcodeParser#statement.
    def enterStatement(self, ctx: lolcodeParser.StatementContext):
        pass

    # Exit a parse tree produced by lolcodeParser#statement.
    def exitStatement(self, ctx: lolcodeParser.StatementContext):
        pass

    # Enter a parse tree produced by lolcodeParser#loop.
    def enterLoop(self, ctx: lolcodeParser.LoopContext):
        self.help_list.append("while ")
        pass

    # Exit a parse tree produced by lolcodeParser#loop.
    # powinnam tutaj dodawać label z po wile coś tam coś tam
    def exitLoop(self, ctx: lolcodeParser.LoopContext):

        if ctx.getChild(self, 1) == ctx.getChild(self, ctx.getChildCount(self)-1):
            self.help_list.append("break")
        pass

    # Enter a parse tree produced by lolcodeParser#declaration.
    def enterDeclaration(self, ctx: lolcodeParser.DeclarationContext):
        pass

    # Exit a parse tree produced by lolcodeParser#declaration.
    def exitDeclaration(self, ctx: lolcodeParser.DeclarationContext):
        pass

    # Enter a parse tree produced by lolcodeParser#comment.
    def enterComment(self, ctx: lolcodeParser.CommentContext):
        if ctx.getChild(self, 0) == 'BTW':
            self.help_list.append('#')
        elif ctx.getChild(self, 0) == 'OBTW':
            self.help_list.append("'''")

    # Exit a parse tree produced by lolcodeParser#comment.
    # how to invalidate the insides?
    def exitComment(self, ctx: lolcodeParser.CommentContext):
        if ctx.getChild(ctx.getChildCount()-1) == 'TLDR':
            self.help_list.append("'''")
        pass

    # Enter a parse tree produced by lolcodeParser#print_block.
    def enterPrint_block(self, ctx: lolcodeParser.Print_blockContext):
        self.help_list.append("print(")
        pass

    # Exit a parse tree produced by lolcodeParser#print_block.
    def exitPrint_block(self, ctx: lolcodeParser.Print_blockContext):
        for i in range(self.help_list[::-1].index("print("), len(self.help_list)-2):
            self.help_list[i] = self.help_list[i]+" +"
        self.help_list.append(")")

    # Enter a parse tree produced by lolcodeParser#if_block.
    # chyba to ma tak działac, ale nie jestem pewna
    def enterIf_block(self, ctx: lolcodeParser.If_blockContext):
        #self.help_list.append("if "+self.help_list[-1]+":")
        pass

    # Exit a parse tree produced by lolcodeParser#if_block.
    def exitIf_block(self, ctx: lolcodeParser.If_blockContext):
        pass

    # Enter a parse tree produced by lolcodeParser#else_if_block.
    def enterElse_if_block(self, ctx: lolcodeParser.Else_if_blockContext):
        pass

    # Exit a parse tree produced by lolcodeParser#else_if_block.
    def exitElse_if_block(self, ctx: lolcodeParser.Else_if_blockContext):
        pass

    # Enter a parse tree produced by lolcodeParser#input_block.
    def enterInput_block(self, ctx: lolcodeParser.Input_blockContext):
        pass

    # Exit a parse tree produced by lolcodeParser#input_block.
    def exitInput_block(self, ctx: lolcodeParser.Input_blockContext):
        self.help_list.append(" = input()")
        pass

    # Enter a parse tree produced by lolcodeParser#func_decl.
    def enterFunc_decl(self, ctx: lolcodeParser.Func_declContext):
        pass

    # Exit a parse tree produced by lolcodeParser#func_decl.
    def exitFunc_decl(self, ctx: lolcodeParser.Func_declContext):
        pass

    # Enter a parse tree produced by lolcodeParser#assignment.
    def enterAssignment(self, ctx: lolcodeParser.AssignmentContext):
        pass

    # Exit a parse tree produced by lolcodeParser#assignment.
    def exitAssignment(self, ctx: lolcodeParser.AssignmentContext):
        pass

    # Enter a parse tree produced by lolcodeParser#expression.
    def enterExpression(self, ctx: lolcodeParser.ExpressionContext):
        # tutaj mogę sprawdzić, czy expression jest bool albo null albo coś takiego, i zamienić to na false
        if ctx.getChildCount() == 1:
            if 'FAIL' in ctx.getText():
                self.help_list.append("False ")
                pass
            elif 'WIN' in ctx.getText():
                self.help_list.append("True ")
                pass
            elif 'NOOB' in ctx.getText():
                self.help_list.append("None ")
                pass
        pass

    # Exit a parse tree produced by lolcodeParser#expression.
    def exitExpression(self, ctx: lolcodeParser.ExpressionContext):
        pass

    # Enter a parse tree produced by lolcodeParser#equals.
    def enterEquals(self, ctx: lolcodeParser.EqualsContext):
        pass

    # Exit a parse tree produced by lolcodeParser#equals.
    def exitEquals(self, ctx: lolcodeParser.EqualsContext):
        pass

    # Enter a parse tree produced by lolcodeParser#not_equals.
    def enterNot_equals(self, ctx: lolcodeParser.Not_equalsContext):
        pass

    # Exit a parse tree produced by lolcodeParser#not_equals.
    def exitNot_equals(self, ctx: lolcodeParser.Not_equalsContext):
        pass

    # Enter a parse tree produced by lolcodeParser#both.
    def enterBoth(self, ctx: lolcodeParser.BothContext):
        pass

    # Exit a parse tree produced by lolcodeParser#both.
    def exitBoth(self, ctx: lolcodeParser.BothContext):
        pass

    # Enter a parse tree produced by lolcodeParser#either.
    def enterEither(self, ctx: lolcodeParser.EitherContext):
        pass

    # Exit a parse tree produced by lolcodeParser#either.
    def exitEither(self, ctx: lolcodeParser.EitherContext):
        pass

    # Enter a parse tree produced by lolcodeParser#greater.
    def enterGreater(self, ctx: lolcodeParser.GreaterContext):
        pass

    # Exit a parse tree produced by lolcodeParser#greater.
    def exitGreater(self, ctx: lolcodeParser.GreaterContext):
        pass

    # Enter a parse tree produced by lolcodeParser#less.
    def enterLess(self, ctx: lolcodeParser.LessContext):
        pass

    # Exit a parse tree produced by lolcodeParser#less.
    def exitLess(self, ctx: lolcodeParser.LessContext):
        pass

    # Enter a parse tree produced by lolcodeParser#add.
    def enterAdd(self, ctx: lolcodeParser.AddContext):
        pass

    # Exit a parse tree produced by lolcodeParser#add.
    def exitAdd(self, ctx: lolcodeParser.AddContext):
        pass

    # Enter a parse tree produced by lolcodeParser#sub.
    def enterSub(self, ctx: lolcodeParser.SubContext):
        pass

    # Exit a parse tree produced by lolcodeParser#sub.
    def exitSub(self, ctx: lolcodeParser.SubContext):
        pass

    # Enter a parse tree produced by lolcodeParser#mul.
    def enterMul(self, ctx: lolcodeParser.MulContext):
        pass

    # Exit a parse tree produced by lolcodeParser#mul.
    def exitMul(self, ctx: lolcodeParser.MulContext):
        pass

    # Enter a parse tree produced by lolcodeParser#div.
    def enterDiv(self, ctx: lolcodeParser.DivContext):
        pass

    # Exit a parse tree produced by lolcodeParser#div.
    def exitDiv(self, ctx: lolcodeParser.DivContext):
        pass

    # Enter a parse tree produced by lolcodeParser#mod.
    def enterMod(self, ctx: lolcodeParser.ModContext):
        pass

    # Exit a parse tree produced by lolcodeParser#mod.
    def exitMod(self, ctx: lolcodeParser.ModContext):
        self.help_list
        pass

    # Enter a parse tree produced by lolcodeParser#cast.
    def enterCast(self, ctx: lolcodeParser.CastContext):
        pass

    # Exit a parse tree produced by lolcodeParser#cast.
    def exitCast(self, ctx: lolcodeParser.CastContext):
        pass

    # Enter a parse tree produced by lolcodeParser#all.
    def enterAll(self, ctx: lolcodeParser.AllContext):
        self.help_list.add("all")


    # Exit a parse tree produced by lolcodeParser#all.
    def exitAll(self, ctx: lolcodeParser.AllContext):
        for i in range(self.help_list[::-1].index("all"), len(self.help_list)-2):
            self.help_list[i] = self.help_list[i]+" and"
        del self.help_list[self.help_list[::-1].index("all")]
        self.help_list.append(")")


    # Enter a parse tree produced by lolcodeParser#any.
    def enterAny(self, ctx: lolcodeParser.AnyContext):
        self.help_list.add("any")


    # Exit a parse tree produced by lolcodeParser#any.
    def exitAny(self, ctx: lolcodeParser.AnyContext):
        for i in range(self.help_list[::-1].index("any"), len(self.help_list)-2):
            self.help_list[i] = self.help_list[i]+" or"
        del self.help_list[self.help_list[::-1].index("any")]
        self.help_list.append(")")


    # DONE Enter a parse tree produced by lolcodeParser#nope.
    def enterNope(self, ctx: lolcodeParser.NopeContext):
        self.help_list.append("not ")
        print("not" + ctx.getText())
        pass

    # DONE Exit a parse tree produced by lolcodeParser#nope.
    def exitNope(self, ctx: lolcodeParser.NopeContext):
        pass

    # Enter a parse tree produced by lolcodeParser#func.
    def enterFunc(self, ctx: lolcodeParser.FuncContext):
        pass

    # Exit a parse tree produced by lolcodeParser#func.
    def exitFunc(self, ctx: lolcodeParser.FuncContext):
        pass
