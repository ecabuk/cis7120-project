# Generated from Ismo.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("=\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\7\2\16\n")
        buf.write("\2\f\2\16\2\21\13\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\7\4!\n\4\f\4\16\4$\13\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\7\5,\n\5\f\5\16\5/\13\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6;\n\6\3\6\2\4\6\b\7\2\4")
        buf.write("\6\b\n\2\2\2?\2\17\3\2\2\2\4\22\3\2\2\2\6\27\3\2\2\2\b")
        buf.write("%\3\2\2\2\n:\3\2\2\2\f\16\5\4\3\2\r\f\3\2\2\2\16\21\3")
        buf.write("\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2\20\3\3\2\2\2\21\17\3")
        buf.write("\2\2\2\22\23\7\n\2\2\23\24\7\3\2\2\24\25\5\6\4\2\25\26")
        buf.write("\7\4\2\2\26\5\3\2\2\2\27\30\b\4\1\2\30\31\5\b\5\2\31\"")
        buf.write("\3\2\2\2\32\33\f\5\2\2\33\34\7\5\2\2\34!\5\b\5\2\35\36")
        buf.write("\f\4\2\2\36\37\7\6\2\2\37!\5\b\5\2 \32\3\2\2\2 \35\3\2")
        buf.write("\2\2!$\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#\7\3\2\2\2$\"\3\2")
        buf.write("\2\2%&\b\5\1\2&\'\5\n\6\2\'-\3\2\2\2()\f\4\2\2)*\7\7\2")
        buf.write("\2*,\5\n\6\2+(\3\2\2\2,/\3\2\2\2-+\3\2\2\2-.\3\2\2\2.")
        buf.write("\t\3\2\2\2/-\3\2\2\2\60\61\7\b\2\2\61\62\5\6\4\2\62\63")
        buf.write("\7\t\2\2\63;\3\2\2\2\64\65\7\6\2\2\65;\5\n\6\2\66\67\7")
        buf.write("\5\2\2\67;\5\n\6\28;\7\f\2\29;\7\n\2\2:\60\3\2\2\2:\64")
        buf.write("\3\2\2\2:\66\3\2\2\2:8\3\2\2\2:9\3\2\2\2;\13\3\2\2\2\7")
        buf.write("\17 \"-:")
        return buf.getvalue()


class IsmoParser ( Parser ):

    grammarFileName = "Ismo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'+'", "'-'", "'*'", "'('", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Id", "Letter", "Literal", "NonZeroDigit", "Digit", 
                      "WS" ]

    RULE_prgm = 0
    RULE_asgm = 1
    RULE_exp = 2
    RULE_term = 3
    RULE_fact = 4

    ruleNames =  [ "prgm", "asgm", "exp", "term", "fact" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    Id=8
    Letter=9
    Literal=10
    NonZeroDigit=11
    Digit=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class PrgmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asgm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsmoParser.AsgmContext)
            else:
                return self.getTypedRuleContext(IsmoParser.AsgmContext,i)


        def getRuleIndex(self):
            return IsmoParser.RULE_prgm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrgm" ):
                return visitor.visitPrgm(self)
            else:
                return visitor.visitChildren(self)




    def prgm(self):

        localctx = IsmoParser.PrgmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prgm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IsmoParser.Id:
                self.state = 10
                self.asgm()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AsgmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(IsmoParser.Id, 0)

        def exp(self):
            return self.getTypedRuleContext(IsmoParser.ExpContext,0)


        def getRuleIndex(self):
            return IsmoParser.RULE_asgm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsgm" ):
                return visitor.visitAsgm(self)
            else:
                return visitor.visitChildren(self)




    def asgm(self):

        localctx = IsmoParser.AsgmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_asgm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(IsmoParser.Id)
            self.state = 17
            self.match(IsmoParser.T__0)
            self.state = 18
            self.exp(0)
            self.state = 19
            self.match(IsmoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return IsmoParser.RULE_exp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Term_Context(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IsmoParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(IsmoParser.TermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_" ):
                return visitor.visitTerm_(self)
            else:
                return visitor.visitChildren(self)


    class SubContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IsmoParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self):
            return self.getTypedRuleContext(IsmoParser.ExpContext,0)

        def term(self):
            return self.getTypedRuleContext(IsmoParser.TermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub" ):
                return visitor.visitSub(self)
            else:
                return visitor.visitChildren(self)


    class SumContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IsmoParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self):
            return self.getTypedRuleContext(IsmoParser.ExpContext,0)

        def term(self):
            return self.getTypedRuleContext(IsmoParser.TermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSum" ):
                return visitor.visitSum(self)
            else:
                return visitor.visitChildren(self)



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = IsmoParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = IsmoParser.Term_Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 22
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 32
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 30
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = IsmoParser.SumContext(self, IsmoParser.ExpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 24
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 25
                        self.match(IsmoParser.T__2)
                        self.state = 26
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = IsmoParser.SubContext(self, IsmoParser.ExpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 27
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 28
                        self.match(IsmoParser.T__3)
                        self.state = 29
                        self.term(0)
                        pass

             
                self.state = 34
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return IsmoParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IsmoParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(IsmoParser.TermContext,0)

        def fact(self):
            return self.getTypedRuleContext(IsmoParser.FactContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul" ):
                return visitor.visitMul(self)
            else:
                return visitor.visitChildren(self)


    class Fact_Context(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IsmoParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fact(self):
            return self.getTypedRuleContext(IsmoParser.FactContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFact_" ):
                return visitor.visitFact_(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = IsmoParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = IsmoParser.Fact_Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 36
            self.fact()
            self._ctx.stop = self._input.LT(-1)
            self.state = 43
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = IsmoParser.MulContext(self, IsmoParser.TermContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 38
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 39
                    self.match(IsmoParser.T__4)
                    self.state = 40
                    self.fact() 
                self.state = 45
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class FactContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return IsmoParser.RULE_fact

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParenthesesContext(FactContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IsmoParser.FactContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self):
            return self.getTypedRuleContext(IsmoParser.ExpContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentheses" ):
                return visitor.visitParentheses(self)
            else:
                return visitor.visitChildren(self)


    class NegativeContext(FactContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IsmoParser.FactContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fact(self):
            return self.getTypedRuleContext(IsmoParser.FactContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegative" ):
                return visitor.visitNegative(self)
            else:
                return visitor.visitChildren(self)


    class PositiveContext(FactContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IsmoParser.FactContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fact(self):
            return self.getTypedRuleContext(IsmoParser.FactContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPositive" ):
                return visitor.visitPositive(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(FactContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IsmoParser.FactContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Id(self):
            return self.getToken(IsmoParser.Id, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class LiteralContext(FactContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IsmoParser.FactContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Literal(self):
            return self.getToken(IsmoParser.Literal, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)



    def fact(self):

        localctx = IsmoParser.FactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_fact)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IsmoParser.T__5]:
                localctx = IsmoParser.ParenthesesContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.match(IsmoParser.T__5)
                self.state = 47
                self.exp(0)
                self.state = 48
                self.match(IsmoParser.T__6)
                pass
            elif token in [IsmoParser.T__3]:
                localctx = IsmoParser.NegativeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.match(IsmoParser.T__3)
                self.state = 51
                self.fact()
                pass
            elif token in [IsmoParser.T__2]:
                localctx = IsmoParser.PositiveContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.match(IsmoParser.T__2)
                self.state = 53
                self.fact()
                pass
            elif token in [IsmoParser.Literal]:
                localctx = IsmoParser.LiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 54
                self.match(IsmoParser.Literal)
                pass
            elif token in [IsmoParser.Id]:
                localctx = IsmoParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 55
                self.match(IsmoParser.Id)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.exp_sempred
        self._predicates[3] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




