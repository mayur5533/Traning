import pytest


@pytest.mark.Smoke
def test_login():
    print("Login Into System")


@pytest.mark.regressoin
def test_addProduct():
    print("Added Product to the cart")


@pytest.mark.Smoke
def test_logOut():
    print(":Log Out to the system")
