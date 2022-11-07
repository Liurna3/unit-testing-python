
from Resource import *

foo = Resource()

def test_get_name():
    tst = "hola"
    foo.setName(tst)
    assert foo.getName() == tst
