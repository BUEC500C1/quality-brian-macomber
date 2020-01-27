from arabic2Roman import arabic2Roman 

def test1():
    assert arabic2Roman(33) == "XXXIII"

def empty_test():
    assert arabic2Roman() == ""

def max_num():
    assert arabic2Roman(3999) == "MMMCMXCIX"