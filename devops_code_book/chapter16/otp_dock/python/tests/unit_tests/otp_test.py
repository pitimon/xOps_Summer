import pytest
from src import otp

def test_generate_otp_return_str_type():
    res = otp.generate_otp()
    assert type(res) is str

def test_generate_otp_return_length():
    res = otp.generate_otp()
    assert len(res) == 6

def test_generate_otp_return_str_numeric():
    res = otp.generate_otp()
    assert res.isnumeric() == True

def test_generate_otp_return_random():
    res1 = otp.generate_otp()
    res2 = otp.generate_otp()
    assert res1 != res2

@pytest.mark.parametrize("input, output", [('nuttachot@hotmail.com', True), ('nuttachot', False), ('nuttachot.hotmail.com', False)])
def test_val_email(input, output):
    add = otp.val_email(input)
    assert add == output

def test_get_email_list_key_is_not_empty():
    res = otp.get_email_list_key()
    assert res != None
    
def test_get_email_list_key_return_string():
    res = otp.get_email_list_key()
    assert type(res) is str