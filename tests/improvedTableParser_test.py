# test improvedTableParser
from assertpy import assert_that
from models.lineReader import LineReader
from models.improvedTableParser import ImprovedTableParser

def test_improvedTableParser_normal():
	lines = ["select * from abc"]

	tableParser = ImprovedTableParser(LineReader(lines))

	results = tableParser.parse()
	assert_that(results).contains(('abc', 1))

def test_improvedTableParser_multiple():
	lines = ["select * from abc", 
	"select * from acd",
	"select * from",
	"abd"]

	tableParser = ImprovedTableParser(LineReader(lines))

	results = tableParser.parse()
	assert_that(results).contains(('abc', 1))
	assert_that(results).contains(('acd', 1))
	assert_that(results).contains(('abd', 1))

