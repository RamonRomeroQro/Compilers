
import ply.yacc as yacc
import logging
from lexical import LexicalAnalizer
tokens=LexicalAnalizer.tokens

def p_PROGRAM(p):
    '''
    PROGRAM         : COMPSTMT
    '''
    pass

def p_COMPSTMT(p):
    '''
    COMPSTMT        : STMT (TERM EXPR)* TERM
    '''
    pass

def p_STMT(p):
    '''
    STMT            : EXPR
    '''
    pass

def p_EXPR(p):
    '''
    EXPR        : EXPR and EXPR
                | EXPR or EXPR
                | not EXPR
                | ARG
    '''
    pass

def p_ARG(p):
    '''
    ARG         : LHS `=' ARG
                | ARG `+' ARG
                | ARG `-' ARG
                | ARG `*' ARG
                | ARG `/' ARG
                | ARG `%' ARG
                | ARG `**' ARG
                | ARG `>' ARG
                | ARG `>=' ARG
                | ARG `<' ARG
                | ARG `<=' ARG
                | ARG `==' ARG
                | ARG `!=' ARG
                | `!' ARG
                | PRIMARY
    '''
    pass



def p_PRIMARY(p):
    '''
    PRIMARY     : `(' COMPSTMT `)'
                | LITERAL
                | VARIABLE
                | if EXPR THEN
                  COMPSTMT
                  else COMPSTMT
                  end
                | if EXPR THEN
                  COMPSTMT
                  end
                | while EXPR TERM COMPSTMT end

    '''
    pass

def p_LHS(p):
    '''
    LHS             : VARNAME
    '''
    pass

def p_VARIABLE(p):
    '''
    VARIABLE    : VARNAME
                | true
                | false
    '''
    pass



def p_LITERAL(p):
    '''
    LITERAL     : numeric
                | STRING
    '''
    pass
    
def p_STRING(p):
    '''
    STRING          : LITERAL_STRING+
    '''
    pass

def p_TERM(p):
    '''
    TERM            : `;'
                    | `\n'
    '''
    pass

def p_VARNAME(p):
    '''
    VARNAME         : identifier
    '''
    pass

def p_LITERAL_STRING(p):
    '''
    LITERAL_STRING  : `"' any_char* `"'
                    | `'' any_char* `''
                    | ``' any_char* ``'
    '''


def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = open("./tests/9.rb", 'r')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
#Grammar for language(Assignment,Selection & loop)

