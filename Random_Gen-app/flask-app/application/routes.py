from flask import Flask, request, render_template,jsonify
from application import app
import requests
import random


@app.route('/RandNum', methods=['GET', 'POST'])
def RandNum():
	Rand_int=''
	for i in range(10):
		Rand_int += str(random.randint(0,9))
	return Rand_int


@app.route('/RandStr', methods=['GET','POST'])
def RandStr():
	Rand_str=''
	Letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for i in range(10):
		Rand_str += ''.join(random.choice(Letters))
	return Rand_str

@app.route('/Prizegen', methods=['GET', 'POST'])
def Prizegen():
	api = 'http://localhost:5000'

	responseNum = requests.get(api + '/RandNum')
	responseStr = requests.get(api + '/RandStr')
	Generator = str(responseStr.text) + str(responseNum.text)
	return Generator
	#return jsonify({'String':responseNum, 'Number':responseStr})
	

@app.route('/')
@app.route('/Generator', methods=['GET','POST'])
def Generator():
	api ='http://localhost:5000'
	``
	responseGen = requests.get(api + '/Prizegen')

	if request.method == 'POST': 
		responseGen = request.post(api + '/Prizegen')

	return 

	
	return ""