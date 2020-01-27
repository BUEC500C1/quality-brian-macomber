from arabic2Roman import arabic2Roman 

def test1():
    assert arabic2Roman(33) == "XXXIII"

def test_empty():
    assert arabic2Roman('') == ""

def test_maxnum():
    assert arabic2Roman(3999) == "MMMCMXCIX"