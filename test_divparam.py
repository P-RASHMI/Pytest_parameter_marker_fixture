'''
@Author: Rashmi
@Date: 2021-09-30 20:17
@Last Modified by: Rashmi
@Last Modified time: 2021-09-30 20:20
@Title :Example to perform test cases using parameterized test'''

import pytest
@pytest.mark.parametrize("num,output",[(1,11,),(2,22),(3,35),(4,44)])
def test_multiplication_11(num,output):
    '''
    Description :this parametrize test case checks 
    whether given input number multiplied by 11 gives the expected output
    '''
    assert 11 * num == output