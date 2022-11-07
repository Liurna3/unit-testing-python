
from Project import *

foo = Project()

def test_get_name():
    tst = "carlos perez"
    foo.setName(tst)
    assert foo.getName() == tst

def test_get_the_resources():
    tst = "recursos"
    foo.setTheResources(tst)
    assert foo.getTheResources() == tst

def test_get_the_employees():
    tst = "empleados"
    foo.setTheEmployees(tst)
    assert foo.getTheEmployees() == tst

def test_get_the_work_breakdown_structure():
    tst = "tst"
    foo.setTheWorkBreakdownStructure(tst)
    assert foo.getTheWorkBreakdownStructure() == tst
