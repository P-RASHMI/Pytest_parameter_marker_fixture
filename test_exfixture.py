'''
@Author: Rashmi
@Date: 2021-09-30 20:45
@Last Modified by: Rashmi
@Last Modified time: 2021-09-30 20:55
@Title :Example to perform test cases using fixture concept.'''

import pytest
@pytest.fixture
def input_value():
    '''
    Description: this is fixture which stores resource and this is 
    repeatedly used for other test cases
    '''
    input = 100
    return input

def test_div_5(input_value):
    '''
    Description: this takes value from fixture
    '''
    assert input_value % 5 == 0

def test_div_10(input_value):
    '''
    Description: this takes value from fixture
    '''
    assert input_value % 10 == 0

