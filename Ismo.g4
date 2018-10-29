grammar Ismo;

prgm:   asgm*;

asgm:   Id '=' exp ';';

exp:    exp '+' term        # Sum
   |    exp '-' term        # Sub
   |    term                # term_
   ;

term:   term '*' fact       # Mul
    |   fact                # fact_
    ;

fact:   '(' exp ')'         # parentheses
    |   '-' fact            # negative
    |   '+' fact            # positive
    |   Literal             # literal
    |   Id                  # id
    ;

Id:             Letter (Letter | Digit)*;
Letter:         [a-zA-Z_];
Literal:        '0' | NonZeroDigit Digit*;
NonZeroDigit:   [1-9];
Digit:          [0-9];
WS :            [ \t\r\n]+ -> skip;