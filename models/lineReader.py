
class LineReader:
	def __init__(self, lines):
		self.__lines = lines

	def read(self):
		for line in self.__lines:
			yield line
