#! /usr/bin/env python3

import sys
from parser.IsmoLexer import IsmoLexer
from parser.IsmoParser import IsmoParser
from parser.IsmoVisitor import IsmoVisitor
import antlr4


class Visitor(IsmoVisitor):
    memory = {}

    def visitAsgm(self, ctx: IsmoParser.AsgmContext):
        id_ = ctx.Id().getText()
        val = self.visit(ctx.exp())
        self.memory[id_] = val

        print("%s = %d" % (id_, val), file=sys.stdout)

        return val

    def visitSub(self, ctx: IsmoParser.SubContext):
        left = self.visit(ctx.exp())
        right = self.visit(ctx.term())

        return left - right

    def visitSum(self, ctx: IsmoParser.SumContext):
        left = self.visit(ctx.exp())
        right = self.visit(ctx.term())

        return left + right

    def visitMul(self, ctx: IsmoParser.MulContext):
        left = self.visit(ctx.term())
        right = self.visit(ctx.fact())

        return left * right

    def visitNegative(self, ctx: IsmoParser.NegativeContext):
        fact = self.visit(ctx.fact())

        return - fact

    def visitPositive(self, ctx: IsmoParser.PositiveContext):
        fact = self.visit(ctx.fact())

        return +fact

    def visitParentheses(self, ctx: IsmoParser.ParenthesesContext):
        exp = self.visit(ctx.exp())

        return exp

    def visitLiteral(self, ctx: IsmoParser.LiteralContext):
        return int(ctx.Literal().getText())

    def visitId(self, ctx: IsmoParser.IdContext):
        id_ = ctx.Id().getText()

        if id_ not in self.memory:
            raise Exception('Unassigned variable `%s.`' % id_)

        return self.memory.get(id_)


if __name__ == '__main__':
    input = antlr4.FileStream(sys.argv[1])
    lexer = IsmoLexer(input)
    tokens = antlr4.CommonTokenStream(lexer)
    parser = IsmoParser(tokens)
    tree = parser.prgm()

    eval = Visitor()
    eval.visit(tree)
