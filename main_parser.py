
import sys
from parser import Parser


def main(argv):
    f = argv[1]
    code_file = open(f, 'r').read()
    result = Parser.parse(code_file)
    print(result)

if __name__ == "__main__":
	main(sys.argv)
