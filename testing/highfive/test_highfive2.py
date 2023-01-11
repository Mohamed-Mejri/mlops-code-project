from highfive import is_highfive



def test_105():
    assert is_highfive(105)

def test_100():
    assert not is_highfive(100)

def test_106():
    assert not is_highfive(106)