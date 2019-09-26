
import ply.yacc as yacc
import logging
from lexical import LexicalAnalizer
tokens=LexicalAnalizer.tokens

# precedence = (
#     ('left', 'OP_AND', 'OP_OR'),
#     ('left', 'OP_ASSIGN'),
#     ('nonassoc', 'OP_COMPARE'),
#     ('left', 'OP_MORE_OR_EQUAL', 'OP_MORE_THAN',
#      'OP_LESS_OR_EQUAL', 'OP_LESS_THAN'),
#     ('left', 'OP_PLUS', 'OP_MINUS', 'OP_MOD'),
#     ('left', 'OP_MULT', 'OP_DIVIDE', 'OP_POWER'),
#     ('right', 'OP_NOT'),
#     ('right', 'LBRACKET')
# )
def p_program(p): 
    '''program : statements
	'''

def p_statements(p): 
    '''statements : T statement T statements	
	| T statement T 
	'''
def p_T(p):
	'''T : T newline
	|
	'''

def p_statement(p): 
    '''
    statement   : var_declaration 
                | if_statement
                | while_statement
                | print_statement
                | input_statement
    '''
    

def p_input_statement(p):
    '''
    input_statement : INPUT_I
                    | INPUT_S
    '''
 
def p_print_statement(p): 
    '''
    print_statement : PRINT lit_value SEMICOLON
                    | PRINT expression SEMICOLON
                    | PRINT ID SEMICOLON
    '''

def p_var_declaration(p): 
    '''
    var_declaration : ID ASS_OP lit_value SEMICOLON
		            | ID ASS_OP expression SEMICOLON
                    | ID ASS_OP ID SEMICOLON
                    | ID ASS_OP input_statement SEMICOLON
    '''

def p_if_statement(p): 
    '''
    if_statement : IF expression THEN statements END
		         | IF expression THEN statements ELSE statements END
    '''
    

def p_while_statement(p): 
    '''
    while_statement : WHILE expression DO statements END
    '''

def p_expression(p): 
    '''
    expression      : math_expression
                    | MINUS math_expression
		            | relational_expression
    '''

def p_math_expression(p):
    '''
    math_expression : term PLUS math_expression
                    | term MINUS math_expression
                    | term 
    '''

def p_relational_expression(p):
    '''
    relational_expression : math_expression relational_op math_expression
                          | NOT math_expression
    '''

def p_term(p): 
    '''
    term    : factor TIMES term
            | factor DIVIDE term
            | factor MODULO term
            | factor
    '''


def p_factor(p): 
    '''
    factor : lit_value
            | LPAREN expression RPAREN
            | ID
    '''

def p_relational_op(p): 
    '''
    relational_op   : AND 
                    | OR 
                    | GT 
                    | LT 
                    | GE 
                    | LE
                    | NE
                    | EQ 
    '''
def p_lit_value(p):
    '''
    lit_value   : INTEGER 
                | STRING 
                | BOOL 
    '''

def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = open("./tests/7cycleCondition.rb", 'r')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
#Grammar for language(Assignment,Selection & loop)

