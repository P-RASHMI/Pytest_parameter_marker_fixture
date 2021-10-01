'''
@Author: Rashmi
@Date: 2021-09-30 20:17
@Last Modified by: Rashmi
@Last Modified time: 2021-09-30 20:20
@Title :Example to perform test cases using marker concept.
execution for particular marker is pytest -m <markername> -v'''

import pytest
@pytest.mark.great             #pytest.mark.<markername>
def test_greater():
    '''
    Description : test case checks whether number greater than 100
    '''
    num = 200
    assert num > 100

@pytest.mark.great
def test_greater_equal():       
    '''
    Description : test case checks whether number greater 
    than and equal to 100
    '''
    num = 100
    assert num >= 100

@pytest.mark.others
def test_less():
    '''
    Description : test case checks whether number less than 200
    '''
    num = 100
    assert num < 200
    