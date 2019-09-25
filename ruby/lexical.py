import ply.lex as lex
import sys

class LexicalAnalizer(object):
    '''Class that tokenize input file'''

    # List of token identifiers
    tokens = ('while', 'integer', 'plus', 'minus', 'times', 'divide', 'equals', 'lparen',
              'logic', 'logicnot', 'rparen', 'comment', 'keywords',  'string', 'builtinmethod',
              "gt", "lt", "eq", "ne", "ge", "le", 'newline', 'break',
              'else', 'end', 'if', 'true', 'false', 'do',
              'quotes', 'identifier', "constant", "modulo", "boolean",
              "input_string", "input_integer", "output_string",  "output")

    # tokens = ('WHILE', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS',
    # 'LPAREN', 'LOGIC', 'LOGICNOT', 'RPAREN', 'COMMENT', 'KEYWORDS',
    # 'STRING', 'BUILTINMETHOD', 'GT', 'LT', 'EQ', 'NE', 'GE', 'LE',
    # 'NEWLINE', 'BREAK', 'ELSE', 'END', 'IF', 'TRUE', 'FALSE', 'DO',
    # 'QUOTES', 'IDENTIFIER', 'CONSTANT', 'MODULO', 'BOOLEAN', 'INPUT_STRING',
    # 'INPUT_INTEGER', 'OUTPUT_STRING', 'OUTPUT')

    # Regex rules for simple Tokens
    t_plus = r'\+'
    t_modulo = r'\%'
    t_minus = r'-'
    t_times = r'\*'
    t_divide = r'/'
    t_lparen = r'\('
    t_rparen = r'\)'
    t_equals = r'='
    t_lt = r'\<'
    t_gt = r'\>'
    t_eq = r'\=\='
    t_ne = r'\!\='
    t_ge = r'\>\='
    t_le = r'\<\='
    t_ignore = '[ \t]'
    t_quotes = r'\"'
    t_identifier = r'[a-z_][a-zA-Z0-9_]*'
    t_constant = r'[A-Z]+[a-zA-Z0-9_]*'

    def t_comment(self, t):
        r'\#[^\n]*'
        pass

    def t_comments(self, t):
        r'=begin+([\n]*[A-Za-z0-9]*[^\S\n\t]*)*=end'
        pass

    def t_while(self, t):
        r'while'
        return t

    def t_break(self, t):
        r'break'
        return t

    def t_else(self, t):
        r'else'
        return t

    def t_end(self, t):
        r'end'
        return t

    def t_for(self, t):
        r'for'
        return t

    def t_if(self, t):
        r'if'
        return t

    def t_boolean(self, t):
        r'true|false'
        return t

    def t_do(self, t):
        r'do'
        return t

    def t_logic(self, t):
        r'or|and'
        return t

    def t_logicnot(self, t):
        r'not'
        return t

    def t_number(self, t):
        r'\d+'  
        t.value = int(t.value)
        return t

    def t_input_string(self, t):
        r'gets.chomp' 
        return t

    def t_input_integer(self, t):
        r'gets.chomp.to_i'
        return t

    def t_output_string(self, t):
        r'puts'  
        return t

    def t_output(self, t):
        r'print'
        return t

    def t_string(self, t):
        r'\"[^"]*\"'  
        return t

    # Tracking Line no.s
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        return t

    # Error handler
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Building The Lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Generating tokens
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
