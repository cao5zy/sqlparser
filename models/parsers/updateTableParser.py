# update table parser
import re
linePatten = '''(?<=update)\s+([#|@|\w|.|\[|\]]+)'''
brokenPatten = '''(update)\s*$'''
class UpdateTableParser:
	@property
	def title(self):
		return "Updated Tables:"

	def hasBroken(self, line):
		return re.search(brokenPatten, line.lower()) != None

	def parseLine(self, line):
		return re.findall(linePatten, line.lower())
		