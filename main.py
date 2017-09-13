from models.tableParser import TableParser
from models.twoLinesParser import TwoLinesParser

def main():
    parser = TableParser(TwoLinesParser(getlines()))
    l1 = parser.parse()
    list(map(lambda n:print(n), sorted(l1, key=l1.index)))

def getlines():
    with open('sql.sql') as file:
        lines = []

        line = file.readline()
        while line:
            lines.append(line)
            line = file.readline()

        
        return lines
    
if __name__ == '__main__':
    main()
