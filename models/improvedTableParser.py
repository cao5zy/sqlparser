# improve table parser
import re
from collections import Counter

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



        result1 = list(map(lambda n: (n[0], n[1]), dict(Counter(list(map(lambda n:n.replace('[', '').replace(']', ''), result)))).items()))
        def key(key):
            return key[0]

        return sorted(result1, key=key)

