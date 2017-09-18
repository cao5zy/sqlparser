# test UpdateTableParser
from models.parsers.updateTableParser import UpdateTableParser
from assertpy import assert_that

def test_updateTableParser():
	line = "update ABC"

	parser = UpdateTableParser()

	assert_that(parser.parseLine(line)).contains('abc')
	assert_that(parser.hasBroken(line)).is_equal_to(False)

def test_updateTableParser_temp_table():
	line = "update #abc"

	parser = UpdateTableParser()

	assert_that(parser.parseLine(line)).contains('#abc')
	assert_that(parser.hasBroken(line)).is_equal_to(False)

def test_updateTableParser_variable_table():
	line = "update"

	parser = UpdateTableParser()

	assert_that(parser.parseLine(line)).is_length(0)
	assert_that(parser.hasBroken(line)).is_equal_to(True)
