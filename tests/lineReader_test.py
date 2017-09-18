from assertpy import assert_that
from models.lineReader import LineReader
def test_lineReader():
	lines = ["1", "2", "3"]

	lineReader = LineReader(lines)

	for index, line in enumerate(lineReader.read()):
		index == 0 and assert_that(line).is_equal_to('1')
		index == 1 and assert_that(line).is_equal_to('2')

