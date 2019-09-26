import ply.lex as lex
import sys

class LexicalAnalizer(object):

    # List of token identifiers
    tokens = ('GT', 'LE', 'PRINT', 'INTEGER', 'END',
            'GE', 'LPAREN', 'STRING', 'TIMES', 'OR',
            'NE', 'DIVIDE', 'AND', 'IF', 
            'MODULO', 'BOOL', 'DO', 'ELSE', 'MINUS',
            'SEMICOLON', 'EQ', 'INPUT_S', 'LT', 
            'THEN', 'RPAREN', 'PLUS', 'WHILE', 'NOT',
            'ID', 'ASS_OP', 'INPUT_I', 'newline')
    

    #t_ELSE= r'else'
    #t_IF= r'if'
    t_DIVIDE= r'\/'
    t_TIMES= r'\*'
    t_RPAREN= r'\('
    #t_BOOL= r'true|false'
    t_MINUS= r'\-'
    t_ID= r'[a-z_][a-zA-Z0-9_]*'
    #t_INPUT_S= r'gets.chomp'
    t_GE= r'\>\='
    t_NE= r'\!\='
    t_EQ= r'\=\='
    t_LT= r'\<'
    #t_THEN= r'then'
    t_LE= r'\<\='
    t_AND= r'and'
    t_ASS_OP= r'\='
    #t_DO= r'do'
    #t_WHILE= r'while'
    #t_INPUT_I= r'gets.chomp.to_i'
    t_LPAREN= r'\('
    t_OR= r'or'
    t_GT= r'\>\t'
    t_MODULO= r'\%'
    #t_END= r'end'
    t_PLUS= r'\+'
    t_SEMICOLON= r'\;'
    t_NOT= r'not'
    t_ignore='[ \t]'

    
    def t_WHILE(self, t):
        r'while'
        return t


    def t_ELSE(self, t):
        r'else'
        return t

    def t_THEN(self, t):
        r'then'
        return t

    def t_IF(self, t):
        r'if'
        return t

    def t_END(self, t):
        r'end'
        return t

    def t_DO(self, t):
        r'do'
        return t
    def t_comment(self, t):
        r'\#[^\n]*'
        pass

    def t_comments(self, t):
        r'=begin+([\n]*[A-Za-z0-9]*[^\S\n\t]*)*=end'
        pass

  
    def t_BOOL(self, t):
        r'true|false'
        return t

    def t_INTEGER(self, t):
        r'\d+'  
        t.value = int(t.value)
        return t
        
    def t_INPUT_I(self, t):
        r'gets.chomp.to_i'
        return t
    def t_INPUT_S(self, t):
        r'gets.chomp' 
        return t

    def t_PRINT(self, t):
        r'print'
        return t

    def t_STRING(self, t):
        r'\"[^"]*\"'  
        return t

    # Tracking Line no.s
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        return t

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def tokenize(self, data):
        tkns = []
        self.lexer.input(data)
        while(True):
            tok = self.lexer.token()
            if not tok:
                break
            if(tok.type != 'newline'):
                tkns.append([tok.type, tok.value])

        return(tkns)
