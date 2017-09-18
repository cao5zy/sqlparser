# parse collections
from collections import Counter

def parse(parser, lineReader):
	

    def getLine(line):
    	return line if not parser.hasBroken(line) \
    		else " ".join([line, getLine(lineReader.read())]) \
    		if lineReader.canRead \
    		else line

    lineReader.reset()
    result = []
    while lineReader.canRead:
        result += parser.parseLine(getLine(lineReader.read()))



    result1 = list(map(lambda n: (n[0], n[1]), dict(Counter(list(map(lambda n:n.replace('[', '').replace(']', ''), result)))).items()))
    def key(key):
        return key[0]

    return [(parser.title, "")] + sorted(result1, key=key)


