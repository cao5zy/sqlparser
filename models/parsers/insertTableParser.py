# insert table
import re
linePatten = '''insert\s+into\s+([#|@|\w|.|\[|\]]+)'''
brokenPatten = '''insert\s+into\s*$'''
class InsertTableParser:
	@property
	def title(self):
		return "Inserted Tables:"

	def hasBroken(self, line):
		return re.search(brokenPatten, line.lower()) != None

	def parseLine(self, line):
		return re.findall(linePatten, line.lower())

