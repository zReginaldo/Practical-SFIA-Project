from flask import Flask, request, jsonify, Response
import requests
from os import getenv

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

@app.route('/Prizegen', methods=['GET', 'POST'])
def Prizegen():

	responseNum = requests.get('http://randstr_gen:5001/RandStr')
	responseStr = requests.get('http://randnum_gen:5002/RandNum')
	Generator = str(responseStr.text) + str(responseNum.text)
	return Generator

if __name__ == '__main__':
    app.run(port=5003, host='0.0.0.0')
