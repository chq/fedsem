import pytest
import os


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


def test_count_writers():
    fpath = "data/femnist/data/raw_data/by_write"
    flist = os.listdir(fpath)
    print(len(flist))
    result = {}
    writers = {}
    for fn in flist:
        fnpath = os.path.join(fpath, fn)
        fnlist = os.listdir(fnpath)
        result[fnpath] = len(fnlist)
        for _writer in fnlist:
            writer = _writer.split('_')[1]
            if writer in writers:
                writers.update({writer: writers[writer]+1})
            else:
                writers.update({writer: 1})
        
    print(result)
    print(writers)


