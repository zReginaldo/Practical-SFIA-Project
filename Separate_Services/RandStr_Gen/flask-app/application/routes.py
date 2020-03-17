from flask import Flask, request, render_template
from application import app
import requests
import random

@app.route('/')
@app.route('/RandNum', methods=['POST'])
def RandNum():
	Rand_str=''
	Letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for i in range(10):
		Rand_str += ''.join(random.choice(Letters))
	return render_template('RandStr.html', Title='RandStr', Rand_str=Rand_str)