from assertpy import assert_that
from models.twoLinesParser import TwoLinesParser
from models.tableParser import TableParser

def test_tableparser_one_table():
    twoLinesParser = TwoLinesParser(["select * from abc"])
    result = TableParser(twoLinesParser).parse()

    assert_that("abc").is_equal_to(result[0])

def test_tableparser_two_tables():
    twoLinesParser = TwoLinesParser(["select * from abc Inner Join ccc"])
    result = TableParser(twoLinesParser).parse()

    assert_that(result).contains("abc")
    assert_that(result).contains("ccc")

def test_tableparser_broken_line():
    twoLinesParser = TwoLinesParser(["select * from ", "abc inner join ddd as xxx"])
    result = TableParser(twoLinesParser).parse()

    assert_that(result).contains("abc")
    assert_that(result).contains("ddd")
    assert_that(result).is_length(2)
