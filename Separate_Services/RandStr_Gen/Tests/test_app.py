import pytest 
import app 

def test_app_TestLenght(): 
    assert len(app.RandStr())==10 

def test_app_TestType():
    assert type(app.RandStr())==str
