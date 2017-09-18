# from table parser
import re

linePatten = '''(?<=from|join)\s+([#|@|\w|.|\[|\]]+)'''
brokenPatten = '''(from|join)\s*$'''
class FromTableParser:
	def hasBroken(self, line):
		return re.search(brokenPatten, line) != None

	def parseLine(self, line):
		return re.findall(linePatten, line.lower())

	@property
	def title(self):
		return "From tables"