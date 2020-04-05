from flask import Flask, request, jsonify, Response
import requests
import random
import os
from os import getenv
from os import environ

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
app.config['Version'] = getenv('Version')
Version = app.config['Version']

@app.route('/RandNum', methods=['GET','POST'])
def RandNum():
	Large_Numbers = [ "25" , "50" , "75" , "100" ]
	Numbers = ["25" , "50" , "75" , "100", "1" , "1" , "2" , "2" , "3" , "3" , "4" , "4" , "5" , "5" , "6" , "6" , "7" , "7" , "8" , "8" , "9" , "9" , "10" , "10" ]
	target = random.randint(100, 999)

	print ("Original list is : " + str(Numbers))

	for i in range(0, len(Numbers)): 
		Numbers[i] = int(Numbers[i])

	return str(random.sample(Numbers, 24))



if __name__=='__main__':
  app.run(host='0.0.0.0', port=5002, debug=True)