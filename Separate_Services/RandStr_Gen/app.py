from flask import Flask, request, jsonify, Response
import requests
import random
from os import getenv
app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

@app.route('/')
@app.route('/RandStr', methods=['GET','POST'])
def RandStr():
	Rand_str=''
	Letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for i in range(10):
		Rand_str += ''.join(random.choice(Letters))
	return Rand_str

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5001, debug=True)