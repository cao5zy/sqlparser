from models.tableParser import TableParser
from models.twoLinesParser import TwoLinesParser

def main():
    parser = TableParser(TwoLinesParser(getlines()))
    print(parser.parse())

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
