import pytest

@pytest.fixture
def setup():
    print("Launch browser")
    print("Login")
    print("Browse Products")
    yield   #yield function is used to teardown 
    print("logoff")
    print("Close the browser")

def testAddItem(setup):
    print("Add Item Successfully")

def testRemoveItem(setup):
    print("Remove Item Successfully")