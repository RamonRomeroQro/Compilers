import sys
from lexer import LexicalAnalizer as la


def main(argv):
	f = argv[1]
	code_file = open(f, 'r').read()
	la.input(code_file)
	while 1:
		tok = la.token()
		if not tok:
			break
		print (tok)


if __name__ == "__main__":
	main(sys.argv)