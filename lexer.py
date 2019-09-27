from ply import lex
import sys

# List of token identifiers
tokens = ('GT', 'LE', 'PRINT', 'NUMBER', 'END',
          'GE', 'LPAREN', 'STRING', 'TIMES', 'OR',
          'NE', 'DIVIDE', 'AND', 'IF',
          'MODULO', 'BOOL', 'DO', 'ELSE', 'MINUS',
          'SEMICOLON', 'EQ', 'INPUT_S', 'LT',
          'THEN', 'RPAREN', 'PLUS', 'WHILE', 'NOT',
          'ID', 'ASS_OP', 'INPUT_I', 'NEWLINE')


#t_ELSE= r'else'
#t_IF= r'if'
t_DIVIDE = r'\/'
t_TIMES = r'\*'
t_RPAREN = r'\)'
#t_BOOL= r'true|false'
t_MINUS = r'\-'
t_ID = r'[A-Za-z_][a-zA-Z0-9_]*'
#t_INPUT_S= r'gets.chomp'
t_GE = r'\>\='
t_NE = r'\!\='
t_EQ = r'\=\='
t_LT = r'\<'
#t_THEN= r'then'
t_LE = r'\<\='
t_ASS_OP = r'\='
#t_DO= r'do'
#t_WHILE= r'while'
#t_INPUT_I= r'gets.chomp.to_i'
t_LPAREN = r'\('
t_GT = r'\>'
t_MODULO = r'\%'
#t_END= r'end'
t_PLUS = r'\+'
#t_SEMICOLON = r'\;'
t_ignore = '[ \t]'


def t_SEMICOLON(t):
    r'\;'
    pass


def t_OR(t):
    r'or'
    return t


def t_NOT(t):
    r'not'
    return t


def t_AND(t):
    r'and'
    return t


def t_WHILE(t):
    r'while'
    return t


def t_ELSE(t):
    r'else'
    return t


def t_THEN(t):
    r'then'
    return t


def t_IF(t):
    r'if'
    return t


def t_END(t):
    r'end'
    return t


def t_DO(t):
    r'do'
    return t


def t_comment(t):
    r'\#[^\n]*'

    pass


def t_comments(t):
    r'(?s)\=begin[^\n]*.*?\=end'
    pass


def t_BOOL(t):
    r'true|false'
    return t


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    #t.value = int(t.value)
    return t


def t_INPUT_I(t):
    r'gets.chomp.to_i'
    return t


def t_INPUT_S(t):
    r'gets.chomp'
    return t


def t_PRINT(t):
    r'print'
    return t


def t_STRING(t):
    r'\"[^"]*\"'
    return t

# Tracking Line no.s


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


LexicalAnalizer = lex.lex()
