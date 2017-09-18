# test fromTableParser
from models.parsers.fromTableParser import FromTableParser
from assertpy import assert_that

def test_fromTableParser():
	line = "select * from abc"

	parser = FromTableParser()

	assert_that(parser.parseLine(line)).contains('abc')
	assert_that(parser.hasBroken(line)).is_equal_to(False)

def test_fromTableParser_temp_table():
	line = "select * from #abc"

	parser = FromTableParser()

	assert_that(parser.parseLine(line)).contains('#abc')
	assert_that(parser.hasBroken(line)).is_equal_to(False)

def test_fromTableParser_variable_table():
	line = "select * from @abc"

	parser = FromTableParser()

	assert_that(parser.parseLine(line)).contains('@abc')
	assert_that(parser.hasBroken(line)).is_equal_to(False)
