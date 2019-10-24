
import sys
from parser import Parser


def main(argv):
    '''
    Read from command and parse
    '''

    def inOrderTransversal(node):
        if node!=None:
            inOrderTransversal(node.left)
            print(node.value)
            inOrderTransversal(node.right)


    name = argv[1]
    p = open(name, 'r')
    code_file = p.read()
    p.close()
    result = Parser.parse(code_file)
    print(result)
    stack = [result]
    while stack:
        n=stack.pop()
        if n:
            if n.leaf and not isinstance(n.leaf,type(result)):
                print(n.leaf)
            for i in n.children:
                stack.append(i)



if __name__ == "__main__":
    main(sys.argv)
