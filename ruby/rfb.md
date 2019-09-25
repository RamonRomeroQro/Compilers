PROGRAM         : COMPSTMT

COMPSTMT        : STMT (TERM EXPR)* TERM

STMT            : EXPR

EXPR            : EXPR and EXPR
                | EXPR or EXPR
                | not EXPR
                | ARG


ARG             : LHS `=' ARG
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

PRIMARY         : `(' COMPSTMT `)'
                | LITERAL
                | VARIABLE
                | if EXPR THEN
                  COMPSTMT
                  (elsif EXPR THEN COMPSTMT)*
                  [else COMPSTMT]
                  end
                | while EXPR TERM COMPSTMT end
    
LHS             : VARNAME

VARIABLE        : VARNAME
                | true
                | false

LITERAL         : numeric
                | STRING

STRING          : LITERAL_STRING+

TERM            : `;'
                | `\n'


VARNAME         : identifier

LITERAL_STRING  : `"' any_char* `"'
                | `'' any_char* `''
                | ``' any_char* ``'
