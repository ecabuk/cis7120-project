# Generated from Ismo.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("J\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\t\7\t/\n\t\f\t\16\t\62\13\t\3\n\3\n")
        buf.write("\3\13\3\13\3\13\7\139\n\13\f\13\16\13<\13\13\5\13>\n\13")
        buf.write("\3\f\3\f\3\r\3\r\3\16\6\16E\n\16\r\16\16\16F\3\16\3\16")
        buf.write("\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\3\2\6\5\2C\\aac|\3\2\63;\3\2\62;\5\2")
        buf.write("\13\f\17\17\"\"\2N\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5\37\3\2\2\2\7!\3\2\2")
        buf.write("\2\t#\3\2\2\2\13%\3\2\2\2\r\'\3\2\2\2\17)\3\2\2\2\21+")
        buf.write("\3\2\2\2\23\63\3\2\2\2\25=\3\2\2\2\27?\3\2\2\2\31A\3\2")
        buf.write("\2\2\33D\3\2\2\2\35\36\7?\2\2\36\4\3\2\2\2\37 \7=\2\2")
        buf.write(" \6\3\2\2\2!\"\7-\2\2\"\b\3\2\2\2#$\7/\2\2$\n\3\2\2\2")
        buf.write("%&\7,\2\2&\f\3\2\2\2\'(\7*\2\2(\16\3\2\2\2)*\7+\2\2*\20")
        buf.write("\3\2\2\2+\60\5\23\n\2,/\5\23\n\2-/\5\31\r\2.,\3\2\2\2")
        buf.write(".-\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61\22")
        buf.write("\3\2\2\2\62\60\3\2\2\2\63\64\t\2\2\2\64\24\3\2\2\2\65")
        buf.write(">\7\62\2\2\66:\5\27\f\2\679\5\31\r\28\67\3\2\2\29<\3\2")
        buf.write("\2\2:8\3\2\2\2:;\3\2\2\2;>\3\2\2\2<:\3\2\2\2=\65\3\2\2")
        buf.write("\2=\66\3\2\2\2>\26\3\2\2\2?@\t\3\2\2@\30\3\2\2\2AB\t\4")
        buf.write("\2\2B\32\3\2\2\2CE\t\5\2\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2")
        buf.write("\2FG\3\2\2\2GH\3\2\2\2HI\b\16\2\2I\34\3\2\2\2\b\2.\60")
        buf.write(":=F\3\b\2\2")
        return buf.getvalue()


class IsmoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    Id = 8
    Letter = 9
    Literal = 10
    NonZeroDigit = 11
    Digit = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "';'", "'+'", "'-'", "'*'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "Id", "Letter", "Literal", "NonZeroDigit", "Digit", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "Id", "Letter", "Literal", "NonZeroDigit", "Digit", "WS" ]

    grammarFileName = "Ismo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


