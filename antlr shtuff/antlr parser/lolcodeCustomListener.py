from antlr4 import *
from .lolcodeParser import lolcodeParser
from .lolcodeLexer import lolcodeLexer
from .lolcodeListener import lolcodeListener
import re

# a good idea would probably be to try and implement the printing well

class lolcodeCustomListener(lolcodeListener):
    def enterHi(self, ctx):
        print("Hello %s!" % ctx.ID())

    def __init__(self, output):
        self.output = output

    # def enterName(self, ctx: lolcodeParser.NameContext):
    #     self.output.write("<strong>")
    #
    # def exitName(self, ctx: lolcodeParser.NameContext):
    #     self.output.write(ctx.WORD().getText())
    #     self.output.write("</strong> ")
    #
    # def enterColor(self, ctx: ChatParser.ColorContext):
    #     color = ctx.WORD().getText()
    #     ctx.text = '<span style="color: ' + color + '">'
    #
    # def exitColor(self, ctx: ChatParser.ColorContext):
    #     ctx.text += ctx.message().text
    #     ctx.text += '</span>'
    #
    # def exitEmoticon(self, ctx: ChatParser.EmoticonContext):
    #     emoticon = ctx.getText()
    #
    #     if emoticon == ':-)' or emoticon == ':)':
    #         ctx.text = "🙂"
    #
    #     if emoticon == ':-(' or emoticon == ':(':
    #         ctx.text = "🙁"
    #
    # def enterLink(self, ctx: ChatParser.LinkContext):
    #     ctx.text = '<a href="%s">%s</a>' % (ctx.TEXT()[1], (ctx.TEXT()[0]))
    #
    # def exitMessage(self, ctx: ChatParser.MessageContext):
    #     text = ''
    #
    #     for child in ctx.children:
    #         if hasattr(child, 'text'):
    #             text += child.text
    #         else:
    #             text += child.getText()
    #
    #     if isinstance(ctx.parentCtx, ChatParser.LineContext) is False:
    #         ctx.text = text
    #     else:
    #         self.output.write(text)
    #         self.output.write("</p>")
    #
    # def enterCommand(self, ctx: ChatParser.CommandContext):
    #     if ctx.SAYS() is not None:
    #         self.output.write(ctx.SAYS().getText() + ':' + '<p>')
    #
    #     if ctx.SHOUTS() is not None:
    #         self.output.write(ctx.SHOUTS().getText() + ':' + '<p style="text-transform: uppercase">')
    #
    # def exitChat(self, ctx: ChatParser.ChatContext):
    #     self.output.write("</body></html>")

        # Enter a parse tree produced by lolcodeParser#program.
    def enterProgram(self, ctx: lolcodeParser.ProgramContext):
        pass

        # Exit a parse tree produced by lolcodeParser#program.
    def exitProgram(self, ctx: lolcodeParser.ProgramContext):
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
        pass

    # Exit a parse tree produced by lolcodeParser#loop.
    def exitLoop(self, ctx: lolcodeParser.LoopContext):
        pass

    # Enter a parse tree produced by lolcodeParser#declaration.
    def enterDeclaration(self, ctx: lolcodeParser.DeclarationContext):
        pass

    # Exit a parse tree produced by lolcodeParser#declaration.
    def exitDeclaration(self, ctx: lolcodeParser.DeclarationContext):
        pass

    # Enter a parse tree produced by lolcodeParser#comment.
    def enterComment(self, ctx: lolcodeParser.CommentContext):
        pass

    # Exit a parse tree produced by lolcodeParser#comment.
    def exitComment(self, ctx: lolcodeParser.CommentContext):
        pass

    # Enter a parse tree produced by lolcodeParser#print_block.
    def enterPrint_block(self, ctx: lolcodeParser.Print_blockContext):
        pass

    # Exit a parse tree produced by lolcodeParser#print_block.
    def exitPrint_block(self, ctx: lolcodeParser.Print_blockContext):
        pass

    # Enter a parse tree produced by lolcodeParser#if_block.
    def enterIf_block(self, ctx: lolcodeParser.If_blockContext):
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
        pass

    # Enter a parse tree produced by lolcodeParser#cast.
    def enterCast(self, ctx: lolcodeParser.CastContext):
        pass

    # Exit a parse tree produced by lolcodeParser#cast.
    def exitCast(self, ctx: lolcodeParser.CastContext):
        pass

    # Enter a parse tree produced by lolcodeParser#all.
    def enterAll(self, ctx: lolcodeParser.AllContext):
        pass

    # Exit a parse tree produced by lolcodeParser#all.
    def exitAll(self, ctx: lolcodeParser.AllContext):
        pass

    # Enter a parse tree produced by lolcodeParser#any.
    def enterAny(self, ctx: lolcodeParser.AnyContext):
        pass

    # Exit a parse tree produced by lolcodeParser#any.
    def exitAny(self, ctx: lolcodeParser.AnyContext):
        pass

    # Enter a parse tree produced by lolcodeParser#nope.
    def enterNope(self, ctx: lolcodeParser.NopeContext):
        # emoticon = ctx.getText()
        re.sub(r'NOT', 'not', ctx.getText())
        print("not" + ctx.getText())
        pass

    # Exit a parse tree produced by lolcodeParser#nope.
    def exitNope(self, ctx: lolcodeParser.NopeContext):
        pass

    # Enter a parse tree produced by lolcodeParser#func.
    def enterFunc(self, ctx: lolcodeParser.FuncContext):
        pass

    # Exit a parse tree produced by lolcodeParser#func.
    def exitFunc(self, ctx: lolcodeParser.FuncContext):
        pass
