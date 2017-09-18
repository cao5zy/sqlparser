from models.improvedTableParser import ImprovedTableParser
from models.lineReader import LineReader
import sys

def main():
    parser = ImprovedTableParser(LineReader(getlines()))
    l1 = list(map(lambda n:n.replace('[', '').replace(']', ''), parser.parse()))
    def key(el):
        return el

    list(map(lambda n:print(n), sorted(set(l1), key=key)))

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
