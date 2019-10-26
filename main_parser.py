
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

    print("Abstract Syntax Tree (Leveled BFS)")

    from collections import deque
    s = deque([result])
    while s:
        size = len(s)
        l = []
        for i in range(size):
            #print('<<<<',[str(x) for x in s])
            n = s.popleft()
            if n:
                if n.children:
                    for i in n.children:
                        s.append(i)
                if n.leaf != None:
                    l.append((n.leaf, n.type))

                else:
                    l.append((n.type))

        print(l)


if __name__ == "__main__":
    main(sys.argv)
