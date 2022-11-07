
from Employee import Employee

def test_get_name():
    test = "Carlos Peréz"
    foo = Employee()
    foo.setName("Carlos Peréz")

    assert foo.getName() == "Carlos Peréz"

