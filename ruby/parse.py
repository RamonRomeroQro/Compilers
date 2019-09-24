import ply.yacc as yacc
import logging
from .lexical import LexicalAnalizer
import lexer
tokens=LexicalAnalizer.tokens

#Precedence rules for parsing
precedence = (
    ('left', 'plus', 'minus'),
    ('left', 'times', 'divide'),
)

#Grammar for language(Assignment,Selection & loop)



# Build the parser
parser = yacc.yacc()

s = open('test.rb','r').read()

result = parser.parse(s)
#print(log)
