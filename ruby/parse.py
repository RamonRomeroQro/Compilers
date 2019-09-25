
import ply.yacc as yacc
import logging
from lexical import LexicalAnalizer
tokens=LexicalAnalizer.tokens


#STATEMENT -> OUTPUT | ASIGN | LOOP | CONDITIONALIFELSE  | epsilon | INPUT
def p_STMT(p):
	
	p[0]=p[1]



# INPUT -> gets.chomp
#        | gets.chomp.to_i

def p_INPUT(p):
	if p[1]=="gets.chomp":
		p[0]="gets.chomp"
	elif p[1] == "gets.chomp.to_i":
		p[0] = "gets.chomp.to_i"


# OUTPUT -> puts STRING 
#         | print INTEGER
#         | print BOOLEAN
#         | print STRING
def p_OUTPUT(p):

	if p[1] == "print":
		p[0]=("print" , str(p[2]))
	elif p[1] == "puts":
		p[0]=("puts" , str(p[2]))

def p_ASIGN(p):
	if p[1]=="=" :
		p[0]=p[1]
	

# STRING  -> STRING
#         | STRING PLUS STRING

def p_STRING(p):
	if p[2]=="+" :
		p[0]=str(p[1])+str(p[3])
	



def p_EVAL(t):
	
	if t[2] == '>'  :
		t[0] = t[1] > t[3]
	elif t[2] == '<':
		t[0] = t[1] < t[3]
	elif t[2] == '>=':
		t[0] = t[1] >= t[3]
	elif t[2] == '<=':
		t[0] = t[1] <= t[3]
	elif t[2] == '==':
		t[0] = t[1] == t[3]
	elif t[2] == '!=':
		t[0] = t[1] != t[3]
	elif t[2] == "and":
		t[0] = t[1] and t[3]
	elif t[2] == "or":
		t[0] = t[1] or t[3]
	elif t[1] == "not":
		t[0]= not t[1]

		

def p_EXPR(p):
	if p[2] == '+':
		p[0]=p[1]+p[2]
	elif p[2]=='-':
		p[0]=p[1]-p[2]
	elif p[2]=='*':
		p[0]=p[1]*p[2]
	elif p[2]=="/":
		p[0]=p[1]/p[2]
	elif p[2]=="%":
		p[0]=p[1]%p[2]

	



# CONDITIONALIFELSE -> if EVALUATION BLOCK else BLOCK end
#                     | if EVALUATION BLOCK end
# LOOP  ->  while EVALUATION do BLOCK end




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

