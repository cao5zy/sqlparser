# improve table parser
import re

linePatten = '''(?<=from|join)\s+([\w|.|\[|\]]+)'''
brokenPatten = '''(from|join)\s*$'''
class ImprovedTableParser:
    def __init__(self, lineParser):
        self.lineParser = lineParser

    def parse(self):
        result = []

        def getLine(line):
        	return line if not hasBroken(line) \
        		else " ".join([line, getLine(self.lineParser.read())]) \
        		if self.lineParser.canRead \
        		else line


        def parseLine(line):
            return re.findall(linePatten, line.lower())

        def hasBroken(line):
            return re.search(brokenPatten, line) != None

        while self.lineParser.canRead:
            result += parseLine(getLine(self.lineParser.read()))

        return list(set(result))

