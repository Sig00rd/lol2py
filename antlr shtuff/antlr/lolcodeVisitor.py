# Generated from /Users/karolinabogacka/PycharmProjects/lol2py/antlr shtuff/lolcode.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .lolcodeParser import lolcodeParser
else:
    from lolcodeParser import lolcodeParser

# This class defines a complete generic visitor for a parse tree produced by lolcodeParser.

class lolcodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by lolcodeParser#program.
    def visitProgram(self, ctx:lolcodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#code_block.
    def visitCode_block(self, ctx:lolcodeParser.Code_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#statement.
    def visitStatement(self, ctx:lolcodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#loop.
    def visitLoop(self, ctx:lolcodeParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#declaration.
    def visitDeclaration(self, ctx:lolcodeParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#comment.
    def visitComment(self, ctx:lolcodeParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#print_block.
    def visitPrint_block(self, ctx:lolcodeParser.Print_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#if_block.
    def visitIf_block(self, ctx:lolcodeParser.If_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#else_if_block.
    def visitElse_if_block(self, ctx:lolcodeParser.Else_if_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#input_block.
    def visitInput_block(self, ctx:lolcodeParser.Input_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#func_decl.
    def visitFunc_decl(self, ctx:lolcodeParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#assignment.
    def visitAssignment(self, ctx:lolcodeParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#full_expression.
    def visitFull_expression(self, ctx:lolcodeParser.Full_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#expression.
    def visitExpression(self, ctx:lolcodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#equals.
    def visitEquals(self, ctx:lolcodeParser.EqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#not_equals.
    def visitNot_equals(self, ctx:lolcodeParser.Not_equalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#both.
    def visitBoth(self, ctx:lolcodeParser.BothContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#either.
    def visitEither(self, ctx:lolcodeParser.EitherContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#greater.
    def visitGreater(self, ctx:lolcodeParser.GreaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#less.
    def visitLess(self, ctx:lolcodeParser.LessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#add.
    def visitAdd(self, ctx:lolcodeParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#sub.
    def visitSub(self, ctx:lolcodeParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#mul.
    def visitMul(self, ctx:lolcodeParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#div.
    def visitDiv(self, ctx:lolcodeParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#mod.
    def visitMod(self, ctx:lolcodeParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#r_all.
    def visitR_all(self, ctx:lolcodeParser.R_allContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#r_any.
    def visitR_any(self, ctx:lolcodeParser.R_anyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#nope.
    def visitNope(self, ctx:lolcodeParser.NopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#func.
    def visitFunc(self, ctx:lolcodeParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lolcodeParser#r_an.
    def visitR_an(self, ctx:lolcodeParser.R_anContext):
        return self.visitChildren(ctx)



del lolcodeParser