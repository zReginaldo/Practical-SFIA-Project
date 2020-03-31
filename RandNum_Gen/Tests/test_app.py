import pytest 
import app 

def test_app_RandNum0(): 
    assert len(app.RandNum())==10 

def test_app_RandNum1():
    assert type(app.RandNum())==str 
