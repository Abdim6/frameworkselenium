from lib2to3.pgen2 import driver
from selenium import webdriver
import pytest

@pytest.fixture
def setup():
    driver=webdriver.Chrome()
    return driver