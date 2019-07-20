import pytest

from compiler import compile


@pytest.mark.parametrize(
    'string,result',
    [('1 + 3', 4),
     ('1 * 2 + 3', 5),
     ('2 * 3 + 10 / 5 - 2', 6)]
)
def test_common_operations(string, result):
    assert compile(string) == result


@pytest.mark.parametrize(
    'string,result',
    [('(1 + 3) * 2', 8),
     ('2 * (2 + 3) / (10 - 2 * 4) ', 5),
     ('2 * (2 + 10 / (5 - 3))', 14),
     ('2 * ((2 + 10) / (5 - 2))', 8)]
)
def test_operations_with_parenthesis(string, result):
    assert compile(string) == result


@pytest.mark.parametrize(
    'string,result',
    [('-1 + 3 * 2', 5),
     ('2 * - (2 + 3)', -10),
     ('3 * -3 ', -9),
     ('3 - -3 ', 6),
     ('3 - (-3) ', 6),
     ('3 + -3 ', 0),
     ('3 / -3 ', -1)]
)
def test_operations_with_negative_numbers(string, result):
    assert compile(string) == result


@pytest.mark.parametrize(
    'string',
    ['1**2', '1*)', '1*.1', '1.*1', '1*+1', '1+*1', '1*/1', '1/*1',
     '1++1', '1+)', '1+.2', '1.+2', '1+/1', '1/+2',
     '1//2', '1/)2', '1/.1', '1./2',
     '1-)', '2-.1', '1.-2',
     '1..2', '2.)1', '1).2',
     '1+', '1-', '1*', '1/', '1.',
     '1a+2', 'b2', 'c/a', '2*b']

)
def test_syntax_validation_errors(string):
    pytest.raises(SyntaxError, compile, string)
