from hello import *

def test_first():
    output = add_two_numbers(3,5)
    assert output == 8

def test_second():
    output = add_two_numbers(3,5)
    assert output != 9

# def test_multiply():
#     output = multiply_two_numbers(3,5)
#     assert output == 15