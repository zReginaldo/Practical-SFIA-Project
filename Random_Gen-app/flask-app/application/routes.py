from application import app
from flask import Flask, request, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import SubmitField
import wtforms.validators
import requests
import random


@app.route('/large_num', methods=['GET', 'POST'])
def large_num():
	
	large_numbers = '15'+ '25' + '50' + '75' + '100'
	rand_large = (large_numbers)
	return str (rand_large)

@app.route('/small_num', methods=['GET', 'POST'])
def small_num(): 

	small_numbers = '1' + '2' + '3'+ '4' + '5' + '6'+ '7' + '8' + '9' + '10'+ '12' + '14' + '16' + '18' + '20' 
	rand_small = (small_numbers)
	return str (rand_small)

@app.route('/target_num', methods=['GET', 'POST'])
def target_num():

	target = random.randint(1, 999)
	return str ([target])





@app.route('/Vowels', methods=['GET','POST'])
def Vowels():

	vowels = 'A'+ 'E'+ 'I' + 'O' + 'U'
	return vowels

@app.route('/Consonants', methods=['GET','POST'])
def Consonants():

	consonants = 'B' + 'C' + 'D'  + 'F' +'G' + 'H' +'J' + 'K' + 'L' + 'M' + 'N' + 'O' + 'P' + 'Q' +'R' + 'S' + 'T' + 'V' + 'W' + 'X' + 'Y' + 'Z'
	return consonants






''''app.route('/numbers_game', methods=['GET', 'POST'])
def numbers_game():
	api = 'http://localhost:5000'
	small_nums = str(requests.get(api + '/small_num').text)
	large_nums= str(requests.get(api + '/large_num').text)
	target_num = str(requests.get(api + '/target_num').text)


	small = (small_nums)
	large = (large_nums)

	return str(small)'''


'''@app.route('/letters_game', methods=['GET', 'POST'])
def letters_game():
	api = 'http://localhost:5000'
	Vowels = str(requests.get(api + '/Vowels').text)
	Consonants= str(requests.get(api + '/Consonants').text)
	target_Word = str(requests.get(api + '/target_Word').text)'''

	#return str(Consonants)




app.config['SECRET_KEY'] = 'YEsssssMateee'

class Create_Letters(FlaskForm):
	Create_Letters = SubmitField('Generate Letters!!')

class Create_Numbers(FlaskForm):
	Create_Numbers = SubmitField('Generate Numbers!!')
	Target_Number = SubmitField('Generate Target Number')


@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')


@app.route('/Letters', methods=['GET','POST'])
def Letters():
	global letters
	form = Create_Letters()
	api = 'http://localhost:5000'
	
	vowels_pile = str(requests.get(api + '/Vowels').text)
	consonants_pile = str(requests.get(api + '/Consonants').text)
	more_vowels, more_consonants = random.choice([(2, 0), (1, 1), (0, 2)])
	nvowels = 3 + more_vowels
	nconsonants = 4 + more_consonants
	letters = random.sample(vowels_pile, nvowels)
	letters += random.sample(consonants_pile, nconsonants)
	
	return render_template('Letters.html',form=form, letters=letters)

@app.route ('/Numbers', methods=['GET','POST'])
def Numbers():
	global numbers
	form = Create_Numbers()
	api = 'http://localhost:5000'

	vowels_pile = str(requests.get(api + '/small_num').text)
	consonants_pile = str(requests.get(api + '/large_num').text)
	more_vowels, more_consonants = random.choice([(2, 0), (1, 1), (0, 2)])
	nvowels = 3 + more_vowels
	nconsonants = 4 + more_consonants
	numbers = random.sample(str(vowels_pile), nvowels)
	numbers += random.sample(str(consonants_pile), nconsonants)

	Target_number = str(requests.get(api + '/target_num').text)
	
	
	return render_template('Numbers.html',form=form, numbers=numbers, Target_number=Target_number)




@app.route ('/letters_round', methods=['GET','POST'])
def play_letters_round():
	vowels_pile = 'A'+ 'E'+ 'I' + 'O' + 'U'
	consonants_pile = 'B' + 'C' + 'D'  + 'F' +'G' + 'H' +'J' + 'K' + 'L' + 'M' + 'N' + 'O' + 'P' + 'Q' +'R' + 'S' + 'T' + 'V' + 'W' + 'X' + 'Y' + 'Z'

	more_vowels, more_consonants = random.choice([(2, 0), (1, 1), (0, 2)])
	nvowels = 3 + more_vowels
	nconsonants = 4 + more_consonants
	letters = random.sample(vowels_pile, nvowels)
	letters += random.sample(consonants_pile, nconsonants)
	return str(letters)
