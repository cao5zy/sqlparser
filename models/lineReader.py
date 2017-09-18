
class LineReader:
	def __init__(self, lines):
		self.__lines = lines
		self.__index = -1

	@property
	def canRead(self):
		return len(self.__lines) > 0 and self.__index < len(self.__lines) - 1

	def read(self):
		def readLine():
			self.__index += 1
			return self.__lines[self.__index]

		return readLine() if self.canRead else None

	def reset(self):
		self.__index = -1