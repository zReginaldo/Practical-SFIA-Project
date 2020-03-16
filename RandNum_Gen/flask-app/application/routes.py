from flask import Flask, request, render_template
from application import app
import requests
import random

@app.route('/')
@app.route('/RandNum', methods=['POST'])
def RandNum():
	Rand_int=''
	for i in range(10):
		Rand_int += str(random.randint(0,9))
	return render_template('RandNum.html', Title='RandNum', Rand_int=Rand_int)