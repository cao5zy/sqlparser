# test InsertTableParser
from models.parsers.insertTableParser import InsertTableParser
from assertpy import assert_that

def test_insertTableParser():
	line = "insert into ABC"

	parser = InsertTableParser()

	assert_that(parser.parseLine(line)).contains('abc')
	assert_that(parser.hasBroken(line)).is_equal_to(False)

def test_insertTableParser_temp_table():
	line = "insert into #abc"

	parser = InsertTableParser()

	assert_that(parser.parseLine(line)).contains('#abc')
	assert_that(parser.hasBroken(line)).is_equal_to(False)

def test_insertTableParser_variable_table():
	line = "insert into"

	parser = InsertTableParser()

	assert_that(parser.parseLine(line)).is_length(0)
	assert_that(parser.hasBroken(line)).is_equal_to(True)
