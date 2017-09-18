from models.parse import parse
from models.lineReader import LineReader
from models.parsers.fromTableParser import FromTableParser
from models.parsers.updateTableParser import UpdateTableParser
from models.parsers.insertTableParser import InsertTableParser
import sys

def main():
    lineReader = LineReader(getlines())
    # l1 = list(map(lambda n:n.replace('[', '').replace(']', ''), parser.parse()))

    with open('output.txt', 'w') as file:
        for val1, val2 in parse(FromTableParser(), lineReader) +\
        parse(UpdateTableParser(), lineReader) + \
        parse(InsertTableParser(), lineReader):
            file.write('%s:%s\n' %(val1, val2))
        # def key(el):
    #     return el

    # list(map(lambda n:print(n), sorted(set(l1), key=key)))

def getlines():
    with open(sys.argv[1]) as file:
        lines = []

        line = file.readline()
        while line:
            lines.append(line)
            line = file.readline()

        
        return lines
    
if __name__ == '__main__':
    main()
