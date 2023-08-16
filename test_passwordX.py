import pytest
from  passwordX import get_sha1_hash, check_password, generate_random_password, multi_word_password

# test hash function
def test_get_sha1_hash():
    assert get_sha1_hash("password") == "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"

def test_check_password():
    assert check_password("password") == 9659365
    assert check_password("") == 0

def test_multi_word_password():
    result = multi_word_password()
    count = 0
    for word in result.split(" "):
        count += 1
    assert count == 3

def test_generate_random_password():
    assert len(generate_random_password(10,1)) == 10
    assert len(generate_random_password(5,2)) == 5
    assert len(generate_random_password(128,3)) == 128