
import sys
from parser import Parser


def main(argv):
    '''
    Read from command and parse
    '''

    name = argv[1]
    p = open(name, 'r')
    code_file = p.read()
    p.close()
    result = Parser.parse(code_file)


if __name__ == "__main__":
    main(sys.argv)
