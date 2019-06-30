from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl

from .lolcodeParser import lolcodeParser
from .lolcodeLexer import lolcodeLexer
from .lolcodeListener import lolcodeListener


class lolcodeCustomListener(lolcodeListener):
    help_list = []
    output_name = ""
    an_stack = []
    add_space = ""

    def __init__(self, output):
        self.output_name = output

        # Enter a parse tree produced by lolcodeParser#program.

    def enterProgram(self, ctx: lolcodeParser.ProgramContext):
        pass

        # Exit a parse tree produced by lolcodeParser#program.

    def exitProgram(self, ctx: lolcodeParser.ProgramContext):
        index = 0
        to_save = []
        while index < len(self.help_list):
            to_save.append(self.help_list[index])
            index += 1
        for symbol in to_save:
            print(symbol, end="")
        with open(self.output_name, 'w') as f:
            for item in self.help_list:
                f.write("%s" % item)

    # Enter a parse tree produced by lolcodeParser#code_block.
    def enterCode_block(self, ctx: lolcodeParser.Code_blockContext):
        pass

    # Exit a parse tree produced by lolcodeParser#code_block.
    def exitCode_block(self, ctx: lolcodeParser.Code_blockContext):
        pass

    # Enter a parse tree produced by lolcodeParser#statement.
    def enterStatement(self, ctx: lolcodeParser.StatementContext):
        if self.add_space:
            self.help_list.append(self.add_space)
        pass

    # Exit a parse tree produced by lolcodeParser#statement.
    def exitStatement(self, ctx: lolcodeParser.StatementContext):
        if "\n" not in self.help_list[-1]:
            self.help_list.append("\n")

    # Enter a parse tree produced by lolcodeParser#loop.
    def enterLoop(self, ctx: lolcodeParser.LoopContext):
        self.help_list.append("while ")
        self.add_space += 4 * " "

    # Exit a parse tree produced by lolcodeParser#loop.
    def exitLoop(self, ctx: lolcodeParser.LoopContext):
        index = max(idx for idx, val in enumerate(self.help_list)
                    if "while" in val)
        for i in range(index, len(self.help_list)):
            if 4 * " " in self.help_list[i]:
                self.help_list[i] = ""
            if '\n' in self.help_list[i] or ',' in self.help_list[i]:
                self.help_list[i] = ":\n"
                break
        if ctx.getChild(1).getText() == ctx.getChild(ctx.getChildCount() - 1).getText():
            self.add_space = self.add_space[:-4]

    # Enter a parse tree produced by lolcodeParser#declaration.
    def enterDeclaration(self, ctx: lolcodeParser.DeclarationContext):
        pass

    # Exit a parse tree produced by lolcodeParser#declaration.
    def exitDeclaration(self, ctx: lolcodeParser.DeclarationContext):
        if ctx.children:
            for index in range(0, len(ctx.children)):
                # LABEL type
                if isinstance(ctx.children[index], TerminalNode):
                    if ctx.children[index].getSymbol().type == 41:
                        self.help_list.append(ctx.children[index].getText())
                    # ATOM type
                    elif ctx.children[index].getSymbol().type == 40:
                        if 'FAIL' in ctx.getText():
                            self.help_list.append("= False ")
                        elif 'WIN' in ctx.getText():
                            self.help_list.append("= True ")
                        elif 'NOOB' in ctx.getText():
                            self.help_list.append("= None ")
                        else:
                            self.help_list.append("= " + ctx.children[index].getText())
                else:
                    if ctx.children[index].LABEL():
                        self.help_list.append(ctx.children[index].getText())
                    # ATOM type
                    elif ctx.children[index].ATOM():
                        if 'FAIL' in ctx.getText():
                            self.help_list.append("= False ")
                        elif 'WIN' in ctx.getText():
                            self.help_list.append("= True ")
                        elif 'NOOB' in ctx.getText():
                            self.help_list.append("= None ")
                        else:
                            self.help_list.append("= " + ctx.children[index].getText())

    # Enter a parse tree produced by lolcodeParser#comment.
    def enterComment(self, ctx: lolcodeParser.CommentContext):
        if 'OBTW' in ctx.getText():
            self.help_list.append("'''\n")
        elif 'BTW' in ctx.getText():
            self.help_list.append('#')

    # Exit a parse tree produced by lolcodeParser#comment.
    def exitComment(self, ctx: lolcodeParser.CommentContext):
        if 'TLDR' in ctx.getText():
            self.help_list.append("'''")

    # Enter a parse tree produced by lolcodeParser#print_block.
    def enterPrint_block(self, ctx: lolcodeParser.Print_blockContext):
        self.help_list.append("print(")

    # Exit a parse tree produced by lolcodeParser#print_block.
    def exitPrint_block(self, ctx: lolcodeParser.Print_blockContext):
        res = len(self.help_list) - 1 - self.help_list[::-1].index("print(")
        for i in range(res + 2, len(self.help_list) - 1):
            self.help_list[i] = self.help_list[i] + " +"
        if "+" in self.help_list[-1]:
            self.help_list[-1] = self.help_list[-1].replace("+", "")
        self.help_list.append(")")

    # Enter a parse tree produced by lolcodeParser#if_block.
    def enterIf_block(self, ctx: lolcodeParser.If_blockContext):
        n_index = max(idx for idx, val in enumerate(self.help_list[:-1])
                      if "\n" in val)
        self.help_list.insert(n_index + 1, "if ")
        for i in range(n_index + 1, len(self.help_list)):
            if 4 * " " in self.help_list[i] or "\n" in self.help_list[i]:
                self.help_list[i] = ""
        self.help_list[-1] = ":\n"
        self.add_space += " " * 4

    # Exit a parse tree produced by lolcodeParser#if_block.
    def exitIf_block(self, ctx: lolcodeParser.If_blockContext):
        self.add_space = self.add_space[:-4]

    # Enter a parse tree produced by lolcodeParser#else_if_block.
    def enterElse_if_block(self, ctx: lolcodeParser.Else_if_blockContext):
        if 'MEBBE' in ctx.getChild(0).getText():
            self.help_list.append(self.add_space[0:len(self.add_space) - 4])
            self.help_list.append("elif ")
        elif 'NO WAI' in ctx.getChild(0).getText():
            self.help_list.append(self.add_space[0:len(self.add_space) - 4])
            self.help_list.append("else: ")
            self.help_list.append("\n")

    # Exit a parse tree produced by lolcodeParser#else_if_block.
    def exitElse_if_block(self, ctx: lolcodeParser.Else_if_blockContext):
        if 'MEBBE' in ctx.getChild(0).getText():
            index = max(idx for idx, val in enumerate(self.help_list)
                        if "elif" in val)
            for i in range(index, len(self.help_list)):
                if 4 * " " in self.help_list[i]:
                    self.help_list[i] = ""
                if '\n' in self.help_list[i] or ',' in self.help_list[i]:
                    self.help_list[i] = ":\n"
                    break

    # Enter a parse tree produced by lolcodeParser#input_block.
    def enterInput_block(self, ctx: lolcodeParser.Input_blockContext):
        pass

    # Exit a parse tree produced by lolcodeParser#input_block.
    def exitInput_block(self, ctx: lolcodeParser.Input_blockContext):
        for index in range(0, len(ctx.children)):
            if ctx.children[index].getSymbol().type == 41:
                self.help_list.append(ctx.children[index].getSymbol().text + " = input()")

    # Enter a parse tree produced by lolcodeParser#func_decl.
    def enterFunc_decl(self, ctx: lolcodeParser.Func_declContext):
        self.help_list.append("def ")
        name = 0
        for index in range(0, len(ctx.children)):
            if isinstance(ctx.children[index], TerminalNode):
                if ctx.children[index].getSymbol().type == 41:
                    if name == 0:
                        self.help_list.append(ctx.children[index].getText())
                        self.help_list.append("(")
                        name = 1
                    else:
                        self.help_list.append(ctx.children[index].getText())
                        self.help_list.append(",")
        self.help_list[-1] = "):\n"
        self.add_space += 4 * " "

    # Exit a parse tree produced by lolcodeParser#func_decl.
    def exitFunc_decl(self, ctx: lolcodeParser.Func_declContext):
        self.add_space = self.add_space[:-4]
        pass

    # Enter a parse tree produced by lolcodeParser#assignment.
    def enterAssignment(self, ctx: lolcodeParser.AssignmentContext):
        name = 0
        for index in range(0, len(ctx.children)):
            if not isinstance(ctx.children[index], TerminalNode):
                if ctx.children[index].LABEL():
                    if name == 0:
                        self.help_list.append(ctx.children[index].getSymbol().text + "= ")
                        name = 1
            else:
                if ctx.children[index].getSymbol().type == 41:
                    if name == 0:
                        self.help_list.append(ctx.children[index].getSymbol().text + "= ")
                        name = 1

    # Exit a parse tree produced by lolcodeParser#assignment.
    def exitAssignment(self, ctx: lolcodeParser.AssignmentContext):
        pass

    # Enter a parse tree produced by lolcodeParser#expression.
    def enterExpression(self, ctx: lolcodeParser.ExpressionContext):
        # tutaj mogę sprawdzić, czy expression jest bool albo null albo coś takiego, i zamienić to na false
        if ctx.ATOM():
            if 'FAIL' in ctx.getText():
                self.help_list.append("False ")
            elif 'WIN' in ctx.getText():
                self.help_list.append("True ")
            elif 'NOOB' in ctx.getText():
                self.help_list.append("None ")
            else:
                self.help_list.append(ctx.ATOM().getText())
        elif ctx.LABEL():
            self.help_list.append(ctx.LABEL().getText())

    # Exit a parse tree produced by lolcodeParser#expression.
    def exitExpression(self, ctx: lolcodeParser.ExpressionContext):
        pass

    # Enter a parse tree produced by lolcodeParser#full_expression.
    def enterFull_expression(self, ctx: lolcodeParser.Full_expressionContext):
        pass

    # Exit a parse tree produced by lolcodeParser#full_expression.
    def exitFull_expression(self, ctx: lolcodeParser.Full_expressionContext):
        self.help_list.append("\n")
        pass

    # Enter a parse tree produced by lolcodeParser#equals.
    def enterEquals(self, ctx: lolcodeParser.EqualsContext):
        self.an_stack.append('equals')

    # Exit a parse tree produced by lolcodeParser#equals.
    def exitEquals(self, ctx: lolcodeParser.EqualsContext):
        pass

    # Enter a parse tree produced by lolcodeParser#not_equals.
    def enterNot_equals(self, ctx: lolcodeParser.Not_equalsContext):
        self.an_stack.append('not_equals')

    # Exit a parse tree produced by lolcodeParser#not_equals.
    def exitNot_equals(self, ctx: lolcodeParser.Not_equalsContext):
        pass

    # Enter a parse tree produced by lolcodeParser#both.
    def enterBoth(self, ctx: lolcodeParser.BothContext):
        self.an_stack.append('both')

    # Exit a parse tree produced by lolcodeParser#both.
    def exitBoth(self, ctx: lolcodeParser.BothContext):
        pass

    # Enter a parse tree produced by lolcodeParser#either.
    def enterEither(self, ctx: lolcodeParser.EitherContext):
        self.an_stack.append('either')

    # Exit a parse tree produced by lolcodeParser#either.
    def exitEither(self, ctx: lolcodeParser.EitherContext):
        pass

    # Enter a parse tree produced by lolcodeParser#greater.
    def enterGreater(self, ctx: lolcodeParser.GreaterContext):
        self.an_stack.append('greater')

    # Exit a parse tree produced by lolcodeParser#greater.
    def exitGreater(self, ctx: lolcodeParser.GreaterContext):
        pass

    # Enter a parse tree produced by lolcodeParser#less.
    def enterLess(self, ctx: lolcodeParser.LessContext):
        self.an_stack.append('smaller')

    # Exit a parse tree produced by lolcodeParser#less.
    def exitLess(self, ctx: lolcodeParser.LessContext):
        pass

    # Enter a parse tree produced by lolcodeParser#add.
    def enterAdd(self, ctx: lolcodeParser.AddContext):
        self.an_stack.append('add')

    # Exit a parse tree produced by lolcodeParser#add.
    def exitAdd(self, ctx: lolcodeParser.AddContext):
        pass

    # Enter a parse tree produced by lolcodeParser#sub.
    def enterSub(self, ctx: lolcodeParser.SubContext):
        self.an_stack.append('sub')

    # Exit a parse tree produced by lolcodeParser#sub.
    def exitSub(self, ctx: lolcodeParser.SubContext):
        pass

    # Enter a parse tree produced by lolcodeParser#mul.
    def enterMul(self, ctx: lolcodeParser.MulContext):
        self.an_stack.append('mul')

    # Exit a parse tree produced by lolcodeParser#mul.
    def exitMul(self, ctx: lolcodeParser.MulContext):
        pass

    # Enter a parse tree produced by lolcodeParser#div.
    def enterDiv(self, ctx: lolcodeParser.DivContext):
        self.an_stack.append('div')

    # Exit a parse tree produced by lolcodeParser#div.
    def exitDiv(self, ctx: lolcodeParser.DivContext):
        pass

    # Enter a parse tree produced by lolcodeParser#mod.
    def enterMod(self, ctx: lolcodeParser.ModContext):
        self.an_stack.append('mod')

    # Exit a parse tree produced by lolcodeParser#mod.
    def exitMod(self, ctx: lolcodeParser.ModContext):
        pass

    # Enter a parse tree produced by lolcodeParser#all.
    def enterR_all(self, ctx: lolcodeParser.R_allContext):
        self.help_list.add("all")

    # Exit a parse tree produced by lolcodeParser#all.
    def exitR_all(self, ctx: lolcodeParser.R_allContext):
        for i in range(self.help_list[::-1].index("all"), len(self.help_list) - 1):
            self.help_list[i] = self.help_list[i] + " and"
        del self.help_list[self.help_list[::-1].index("all")]
        self.help_list.append(")")

    # Enter a parse tree produced by lolcodeParser#any.
    def enterR_any(self, ctx: lolcodeParser.R_anyContext):
        self.help_list.add("any")

    # Exit a parse tree produced by lolcodeParser#any.
    def exitR_any(self, ctx: lolcodeParser.R_anyContext):
        for i in range(self.help_list[::-1].index("any"), len(self.help_list) - 1):
            self.help_list[i] = self.help_list[i] + " or"
        del self.help_list[self.help_list[::-1].index("any")]
        self.help_list.append(")")

    # DONE Enter a parse tree produced by lolcodeParser#nope.
    def enterNope(self, ctx: lolcodeParser.NopeContext):
        self.help_list.append("not ")
        pass

    # DONE Exit a parse tree produced by lolcodeParser#nope.
    def exitNope(self, ctx: lolcodeParser.NopeContext):
        pass

    # Enter a parse tree produced by lolcodeParser#func.
    def enterFunc(self, ctx: lolcodeParser.FuncContext):
        name = 0
        for index in range(0, len(ctx.children)):
            if not isinstance(ctx.children[index], TerminalNode):
                if ctx.children[index].LABEL():
                    if name == 0:
                        self.help_list.append(ctx.children[index].getSymbol().text + "(")
                        name = 1
            else:
                if ctx.children[index].getSymbol().type == 41:
                    if name == 0:
                        self.help_list.append(ctx.children[index].getSymbol().text + "(")
                        name = 1

    # Exit a parse tree produced by lolcodeParser#func.
    def exitFunc(self, ctx: lolcodeParser.FuncContext):
        name = 0
        for index in range(0, len(ctx.children)):
            if not isinstance(ctx.children[index], TerminalNode):
                if ctx.children[index].LABEL():
                    if name == 0:
                        label = ctx.children[index].text
                        name = 1
            else:
                if ctx.children[index].getSymbol().type == 41:
                    if name == 0:
                        label = ctx.children[index].getText()
                        name = 1
        index = max(idx for idx, val in enumerate(self.help_list)
                    if label in val)
        for i in range(index + 1, len(self.help_list)):
            if isinstance(ctx.children[i - index], TerminalNode):
                if not self.help_list[i][-1] == " ":
                    self.help_list[i] = self.help_list[i] + ", "
            if 4 * " " in self.help_list[i]:
                self.help_list[i] = ""
        if "," in self.help_list[-1]:
            self.help_list[-1] = self.help_list[-1].replace(", ", "")
        self.help_list.append(") ")

    # Enter a parse tree produced by lolcodeParser#r_an.
    def enterR_an(self, ctx: lolcodeParser.R_anContext):
        if self.an_stack:
            char = self.an_stack[-1]
            if char == 'div':
                self.help_list.append("/ ")
            elif char == 'equals':
                self.help_list.append("== ")
            elif char == 'not_equals':
                self.help_list.append("!= ")
            elif char == 'both':
                self.help_list.append("and ")
            elif char == 'either':
                self.help_list.append("or ")
            elif char == 'greater':
                self.help_list.append("> ")
            elif char == 'smaller':
                self.help_list.append("< ")
            elif char == 'add':
                self.help_list.append("+ ")
            elif char == 'sub':
                self.help_list.append("- ")
            elif char == 'mul':
                self.help_list.append("* ")
            elif char == 'mod':
                self.help_list.append("% ")

    # Exit a parse tree produced by lolcodeParser#r_an.
    def exitR_an(self, ctx: lolcodeParser.R_anContext):
        pass
