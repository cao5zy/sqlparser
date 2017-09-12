from models.twoLinesParser import TwoLinesParser
from assertpy import assert_that

def test_twolinesparser_has_normal_lines():
    lines = ['1', '2', '3', '4']
    parser = TwoLinesParser(lines)

    assert_that(parser.canRead).is_equal_to(True)
    parser.read()
    assert_that(parser.lineOne).is_equal_to('1')
    assert_that(parser.lineTwo).is_equal_to('2')

    parser.read()
    assert_that(parser.lineOne).is_equal_to('2')
    assert_that(parser.lineTwo).is_equal_to('3')
    
    
    
