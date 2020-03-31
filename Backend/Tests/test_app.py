import pytest 
import app
import requests
from flask import Flask, request
import requests_mock

def test_app_TestUrl_Str():
    response = requests.get('http://51.104.32.90:5001/RandStr')
    assert len(str(response.text)) == 10

def test_app_TestUrl_Num():
    response = requests.get('http://51.104.32.90:5002/RandNum')
    assert len(str(response.text)) == 10

def test_app_TestUrl_Back():
    response = requests.get('http://51.104.32.90:5003/Prizegen')
    assert len(str(response.text)) == 20
