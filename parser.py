
'''
Declaracion de producciones
'''

from ply import yacc
from lexer import tokens
tokens = tokens


# Analisis de presedencia
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

class Node:
    def __init__(self, type, children=None, leaf=None):
        self.type = type
        if children:
            self.children = children
        else:
            self.children = []
        self.leaf = leaf

    def __str__(self):
        return self.type


# Programa tiene statements
def p_program(p):
    '''program : statements
    '''
    p[0] = Node('program', [p[1]])

# Statements, pueden ser uno o mas (bloques)


def p_statements(p):
    '''statements : statement statements	
                    | statement 
    '''
    if(len(p) == 3):
        #print(str(p[2]) , str(p[4]))
        p[0] = Node("statements+statement", [p[1], p[2]])

    elif(len(p) == 2):
        p[0] = Node("single_statement", [p[1]])

# separados por saltos de lineas


# los distintos tipos de statements


def p_statement(p):
    '''
    statement   : var_declaration 
                | if_statement
                | while_statement
                | print_statement
                | input_statement
                | cons_declaration
    '''
    p[0] = Node("statement", [p[1]])

# HASTA AQUI


# leer de consola
def p_input_statement(p):
    '''
    input_statement : INPUT_I
                    | INPUT_S
    '''
    p[0] = Node("input_statement", [], p[1])

# imprimir a consola


def p_print_statement(p):
    '''
    print_statement : PRINT factor 
                    | PRINT expression 

    '''
    p[0] = Node("print_statement", [p[2]], p[1])

# declaracion de variable


def p_var_declaration(p):
    '''
    var_declaration : ID ASS_OP factor 
                    | ID ASS_OP expression 
                    | ID ASS_OP ID 
                    | ID ASS_OP CONSTANT 
                    | ID ASS_OP input_statement 
    '''
    p[0] = Node('var_declaration', [p[3]], p[1]+p[2])
# declaracion de constante


def p_cons_declaration(p):
    '''
    cons_declaration : CONSTANT ASS_OP factor 
                    | CONSTANT ASS_OP expression 
                    | CONSTANT ASS_OP ID 
                    | CONSTANT ASS_OP CONSTANT
                    | CONSTANT ASS_OP input_statement 
    '''
    p[0] = Node('const_declaration', [p[3]], p[1]+p[2])

# Estructura de if, que permite anidacion gracias a los statements (block)


def p_if_statement(p):
    '''
    if_statement : IF expression THEN statements END
                         | IF expression THEN statements ELSE statements END
    '''
    if len(p) == 6:
        p[0] = Node('if_statement', [p[2], p[4]], [p[1], p[3], p[5]])

    elif len(p) == 8:
        p[0] = Node('if_else_statement', [p[2], p[4], p[6]],
                    [p[1], p[3], p[5], p[7]])


# while de if, que permite anidacion gracias a los statements (block)


def p_while_statement(p):
    '''
    while_statement : WHILE expression DO statements END
    '''
    if len(p) == 6:
        p[0] = Node("while_statement", [p[2], p[4]], [p[1], p[3], p[5]])

# expresiones , mathematicas y relacionales (booleanas)


def p_expression(p):
    '''
    expression      : math_expression
                    | MINUS math_expression
                    | relational_expression
    '''
    if len(p) == 2:
        p[0] = Node("expression", [p[1]])
    elif len(p) == 3:
        if p[1] == '-':
            p[0] = Node("expression", [p[2]], p[1])


# romper expresion matematica en suma y resta (binarias)
def p_math_expression(p):
    '''

    math_expression : math_expression PLUS term  
                    | math_expression MINUS term
                    | term 
    '''
    if len(p) == 4:
        p[0] = Node('math_expression', [p[1], p[3]], [p[2]])
    elif len(p) == 2:
        #print('--->', p[1])
        p[0] = Node('math_expression', [p[1]])


def p_term(p):
    '''
    term    : factor TIMES term
            | factor DIVIDE term
            | factor MODULO term
            | factor
    '''
    if len(p) == 2:
        p[0] = Node("term", [p[1]])
    elif len(p) == 4:
        p[0] = Node("term", [p[1], p[3]], p[2])


# expresiones booleanas

def p_relational_expression(p):
    '''
    relational_expression : math_expression AND math_expression
                        | math_expression OR math_expression 
                        | math_expression GT math_expression 
                        | math_expression LT math_expression 
                        | math_expression GE math_expression 
                        | math_expression LE math_expression
                        | math_expression NE math_expression
                        | math_expression EQ math_expression 
                        | NOT math_expression
    '''
    if len(p) == 4:
        p[0] = Node('relational_expression', [p[1], p[3]], p[2])
    elif len(p) == 3:
        if p[1] == "not":
            p[0] = Node('relational_expression', [p[2]], 'not')

# expresiones matematicas de *%/ (binarias)


# Ultimo nivel de expresiones matematicas a valores o parentesis
def p_factor(p):
    '''
    factor : INTEGER
            | STRING
            | BOOL
            | ID
            | CONSTANT
            | LPAREN expression RPAREN

    '''
    if len(p) == 2:
        p[0] = Node("factor", [], [p[1]])
    elif len(p) == 4:
        p[0] = Node("factor", [p[2]], ['(', ')'])


# imprimir error y ubicación


def p_error(p):
    if p == None:
        token = "end of file"
    else:
        token = f"{p.type}({p.value}) on line {p.lineno}"

    print((f"Syntax error: Unexpected {token}"))


# Build the parser
Parser = yacc.yacc()
