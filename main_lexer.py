import sys
from lexer import LexicalAnalizer as la


def main(argv):
	'''
	Read from command and tokenize
	'''
	name = argv[1]
	p = open(name, 'r')
	code_file = p.read()
	p.close()
	la.input(code_file)
	while 1:
		tok = la.token()
		if not tok:
			break
        print(tok)


if __name__ == "__main__":
    main(sys.argv)
