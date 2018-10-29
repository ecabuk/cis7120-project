# Generated from Ismo.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .IsmoParser import IsmoParser
else:
    from IsmoParser import IsmoParser

# This class defines a complete generic visitor for a parse tree produced by IsmoParser.

class IsmoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by IsmoParser#prgm.
    def visitPrgm(self, ctx:IsmoParser.PrgmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IsmoParser#asgm.
    def visitAsgm(self, ctx:IsmoParser.AsgmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IsmoParser#term_.
    def visitTerm_(self, ctx:IsmoParser.Term_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IsmoParser#Sub.
    def visitSub(self, ctx:IsmoParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IsmoParser#Sum.
    def visitSum(self, ctx:IsmoParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IsmoParser#Mul.
    def visitMul(self, ctx:IsmoParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IsmoParser#fact_.
    def visitFact_(self, ctx:IsmoParser.Fact_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IsmoParser#parentheses.
    def visitParentheses(self, ctx:IsmoParser.ParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IsmoParser#negative.
    def visitNegative(self, ctx:IsmoParser.NegativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IsmoParser#positive.
    def visitPositive(self, ctx:IsmoParser.PositiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IsmoParser#literal.
    def visitLiteral(self, ctx:IsmoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IsmoParser#id.
    def visitId(self, ctx:IsmoParser.IdContext):
        return self.visitChildren(ctx)



del IsmoParser