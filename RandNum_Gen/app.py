from flask import Flask, request, jsonify, Response
import requests
import random
from os import getenv

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

@app.route('/RandNum', methods=['GET','POST'])
def RandNum():
	Rand_int=''
	for i in range(10):
		Rand_int += str(random.randint(0,9))
	return Rand_int

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5002, debug=True)
