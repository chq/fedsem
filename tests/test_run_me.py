import pytest


def myfunc():
    raise ValueError("Exception 123 raised")


def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()


def test_print():
    print(f"this is {__file__}")
    with open("where.txt", "a+") as f:
        f.write("abc")
    assert 2 == 2
