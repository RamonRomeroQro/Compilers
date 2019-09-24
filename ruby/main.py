import sys
from .lexical import LexicalAnalizer


def main(argv):
	f = argv[1]
	code_file = open(f, 'r').read()
	l = LexicalAnalizer()
	l.build()
	tks = l.tokenize(code_file)
    # to l
	for x in tks:
		print(x)


if __name__ == "__main__":
	main(sys.argv)

