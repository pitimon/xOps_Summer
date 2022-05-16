import pytest
from src import math

@pytest.mark.add
@pytest.mark.parametrize("input1, input2, output", [(1,2,3),(1,6,7)])
def test_add(input1, input2,output):
    add = math.add(input1, input2)
    assert add == output

@pytest.mark.sub
@pytest.mark.parametrize("input1, input2, output", [(1,2,-1)])
def test_sub(input1, input2,output):
    substract = math.sub(input1, input2)
    assert substract == output
    
def test_sub_return_type():
    substract = math.sub(5, 2)
    assert type(substract) is int
    