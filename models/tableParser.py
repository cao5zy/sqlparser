import re

linePatten = '''(?<=from|join)\s+([\w|.|\[|\]]+)'''
brokenPatten = '''(from|join)\s*$'''
getBrokenPatten = '''^\s*([\w|.|\[|\]]+)'''
class TableParser:
    def __init__(self, twoLinesParser):
        self.twoLinesParser = twoLinesParser

    def parse(self):
        result = []

        def parseLine(line):
            return re.findall(linePatten, line.lower())

        def hasBroken(line):
            return re.search(brokenPatten, line) != None

        def getBroken(line):
            return re.search(getBrokenPatten, line).groups()[0]
        
        parser = self.twoLinesParser
        while parser.canRead:
            parser.read()

            result += parseLine(parser.lineOne)

            if hasBroken(parser.lineOne):
                result.append(getBroken(parser.lineTwo))

            result += parseLine(parser.lineTwo)

        return list(set(result))
