from flask import Flask, request, jsonify, Response
import requests
from os import getenv
from itertools import permutations
from itertools import combinations_with_replacement 
from itertools import product
import random
import json
import os 

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

large_numbers=2 # max allowed 4 min 0
small_numbers=4 # 6 - large number
target_to_hit=0
our_large_numbers=[]
our_small_numbers=[]

global nearest_answer
global nearest_solution

nearest_answer=999999999999
nearest_solution=99999999999

def reversepolishnotation(input1):
    # using Reverse Polish notation
 
    stack = []
 
    for val in input1.split(' '):
        if val in ['-', '+', '*', '/']:
            op1 = stack.pop()
            op2 = stack.pop()
            if op2 > op1:
                if val=='-': result = op2 - op1
            else:
                if val=='-': result = op1 - op2
            if val=='+': result = op2 + op1
            if val=='*': result = op2 * op1
            try:
                if val=='/':
                    check_left_over = op2 % op1
                    if check_left_over==0:
                        result = op2 / op1
                        result = int(result)
                    else:
                        result=999999999999 
            except:
                #catching divide by 0 errors
                result=999999999999 
            stack.append(result)
        else:
            try:
                stack.append(int(val))
            except Exception as e:
                print(e)
                breakpoint()
 
    return stack.pop()

def DefNums(smalln,largen):
	large_numbers=2 # max allowed 4 min 0
	small_numbers=4 # 6 - large number
	target_to_hit=0
	our_large_numbers=[]
	our_small_numbers=[]
	global nearest_answer
	global nearest_solution
	nearest_answer=999999999999
	nearest_solution=99999999999

	url = 'http://51.104.32.215:5002/RandNum'
	Full_Nums = (requests.get(url).text)
	Full_Nums = Full_Nums [1:-1]
	Full_Nums = Full_Nums.replace(" ","")
	Full_Nums = (Full_Nums.split(","))
	large_nums = []
	small_nums = []
	target = random.randint(100,999)

	for i in Full_Nums:
		if i == '25' or i =="50" or i == "75" or i == "100":
			large_nums.append(int(i))
	
	for i in Full_Nums:
		if i == '1' or i =="2" or i == "3" or i == "4" or i == "5" or i == "6" or i =="7" or i == "8" or i == "9" or i =="10":
			small_nums.append(int(i))

	selected_large_numbers=[]
	selected_small_numbers=[]

	target=random.randint(100,999)
	for i in range(largen):
		lnc=random.choice(large_nums)
		selected_large_numbers.append(lnc)
		large_nums.remove(lnc)

	for i in range(smalln):
		snc=random.choice(small_nums)
		selected_small_numbers.append(snc)
		small_nums.remove(snc)
	return (target,selected_large_numbers,selected_small_numbers)

def hownear(target,answer,formula):

    global nearest_answer
    global nearest_solution

    if int(target) == int(answer):
        print ("Woop")
        nearest_answer=answer
        nearest_solution=formula
        return (1)
    else:
        distance=abs(target-answer)
        if distance < abs(nearest_answer-target):
            nearest_answer=answer
            nearest_solution=formula
        return (0)

def make_formula_more_readable(nearest_solution):
	#Make calulation Printable
    tuple_calc = []
    # data in format 
        #{'nearest_solution': '100 5 7 50 4 6 - / * * +'}
    nearest_solution_list=nearest_solution.split(" ")

    digit_solution=[]
    symbol_solution=[]
    for i in nearest_solution_list:
        if i.isdigit():
            digit_solution.append(i)
        else:
            symbol_solution.append(i)

    # data in format:
        #nearest_solution_list': ['100', '5', '7', '50', '4', '6', '-', '/', '*', '*', '+']
        #digit_solution: ['100', '5', '7', '50', '4', '6']
        #symbol_solution': ['-', '/', '*', '*', '+']


    while True:
        #loop until nothing left in symbol_solution, break out at bottom of loop

        # get numbers for caculation
        # 

        lastdigit=digit_solution.pop()
        sec_lastdigit=digit_solution.pop()
        tmp_list=[]
        tmp_list.append(int(lastdigit))
        tmp_list.append(int(sec_lastdigit))
        tmp_list.sort()
        lastdigit=tmp_list[1]
        sec_lastdigit=tmp_list[0]


        #  the above logic helps with if the second number is bigger than first reverse them i.e 2 -100 is revered to 100 - 2 this helps with - and division

        # get symbol for caculation
        l_symbol=symbol_solution.pop(0)
        # data in format
            #'l_symbol': '-'

    
        #calc answer and print 
        if l_symbol=='*':
            answer = int(lastdigit) * int(sec_lastdigit)
        if l_symbol=='/':
            answer = int(lastdigit) / int(sec_lastdigit)
            # make a int i.e 25 rather than a float 25.0
            answer=int(answer)
        if l_symbol=='-':
            answer = int(lastdigit) - int(sec_lastdigit)
        if l_symbol=='+':
            answer = int(lastdigit) + int(sec_lastdigit)

        # put the answer back into the digit list
        digit_solution.append(str(answer))

        Calculation = ("%s %s %s = %s"%(lastdigit,l_symbol,sec_lastdigit,answer))
        tuple_calc.append(Calculation)
        print (Calculation)
        

        if symbol_solution==[]:
            return tuple_calc
    tuple_calc = tuple_calc [1:-1]
    tuple_calc = tuple_calc.replace(" ","")
    tuple_calc = (tuple_calc.split(","))

@app.route('/Numbers', methods=['GET','POST'])
def GetNums(): 
	target_to_hit,our_large_numbers,our_small_numbers=DefNums(smalln=small_numbers,largen=large_numbers)

	numbers_to_use=2

	while (numbers_to_use < 8) or (rv==1) :


    # we have our numbers and the taget lets start getting funcky
		master_numbers=our_large_numbers+our_small_numbers

		# we need 1 less symbol than the number of numbers
		comb_needed=numbers_to_use

		#create all the perumataions of our numbers
		perm = permutations(master_numbers,numbers_to_use)
		comb_needed_m1=numbers_to_use-1
		symbol1 = product(["+", "*", "-","/"],repeat=comb_needed_m1)

		#using permutations inside a nested loop doesn't work as expected so i have taken the smaller permutation and converted into a list
		# might have to test with large datasets as this may slow things down
		symbol2=[]
		for i1 in symbol1:
			t1=i1[0]
			try:
				t2=i1[1]
			except:
				pass
			try:
				t3=i1[2]
			except:
				pass
			try:
				t4=i1[3]
			except:
				pass
			try:
				t5=i1[4]
			except:
				pass
			
			t9=[]
			t9.append(t1)
			try:
				t9.append(t2)
			except: 
				pass
			try:
				t9.append(t3)
			except:
				pass
			try:
				t9.append(t4)
			except:
				pass
			try:
				t9.append(t5)
			except:
				pass

			symbol2.append(t9)

		# pass permutations to memory
		for i in perm:
			fn1=int(i[0])
			fn2=int(i[1])
			try:
				fn3=int(i[2])
			except:
				pass
			try:
				fn4=int(i[3])
			except:
				pass
			try:
				fn5=int(i[4])
			except:
				pass
			try:
				fn6=int(i[5])
			except:
				pass
			for sy1 in symbol2:
				s1=sy1[0]
				try:
					s2=sy1[1]
				except:
					pass
				try:
					s3=sy1[2]
				except:
					pass
				try:
					s4=sy1[3]
				except:
					pass
				try:
					s5=sy1[4]
				except:
					pass
				if numbers_to_use==2:
					expression = "%s %s %s" % (fn1,fn2,s1)
				elif numbers_to_use==3:
					expression = "%s %s %s %s %s" % (fn1,fn2,fn3,s1,s2)
				elif numbers_to_use==4:
					expression = "%s %s %s %s %s %s %s" % (fn1,fn2,fn3,fn4,s1,s2,s3)
				elif numbers_to_use==5:
					expression = "%s %s %s %s %s %s %s %s %s" % (fn1,fn2,fn3,fn4,fn5,s1,s2,s3,s4)
				elif numbers_to_use==6:
					expression = "%s %s %s %s %s %s %s %s %s %s %s" % (fn1,fn2,fn3,fn4,fn5,fn6,s1,s2,s3,s4,s5)
				else:
					print ("Err what")
					breakpoint()


				result = reversepolishnotation(expression)
				#if verbose_output==1:
				#print (expression,result)
					#make_formula_more_readable(expression)
				rv=hownear(target=target_to_hit,answer=result,formula=expression)
				if rv==1:
					break
			if rv==1:
				break
		if rv==1:
			break
		else:
			numbers_to_use+=1
	print ("\nSummary")
	outby=abs(target_to_hit-nearest_answer)
	if outby !=0:
		print ("We were %s out" %(outby))
	else:
		print ("Yep we found the answer :)")
	print ("We tried to hit %s the nearest we could get was %s made up of %s" %(target_to_hit,nearest_answer,nearest_solution))
	make_formula_more_readable(nearest_solution)

	return str(target_to_hit) + str(our_large_numbers) + str(our_small_numbers) +str(make_formula_more_readable(nearest_solution))

@app.route('/Letters', methods=['GET', 'POST'])
def CDLetters(): 
	url = 'http://51.104.32.215:5001/RandStr'
	Full_Letters = (requests.get(url).text)
	vowels = []
	consonants = []

	for i in Full_Letters:
		if i == 'a'or i =="e" or i == "i" or i == "o" or i == "u":
			vowels.append(i)

		for i in Full_Letters:
			if i == 'b'or i == 'c'or i == 'd'or i == 'f'or i == 'g'or i == 'h'or  i == 'j'or i == 'k'or i == 'l'or i == 'm'or i == 'n'or i == 'p'or i == 'q'or i == 'r'or i == 's'or i == 't'or i == 'v' or i == 'w'or i == 'x'or i == 'y'or i == 'z':
				consonants.append(i)
			
	random_letters = random.sample(vowels,2) + random.sample(consonants, 7)
	vowels = ['a', 'e', 'i', 'o', 'u']

	inputLetters = random_letters
	print(inputLetters)

	#Make list of the other 17 letters as notInputLetters
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	notInputLetters = []

	for w in alphabet:
		if w not in inputLetters:
			notInputLetters.append(w)

	#Import OLD wordlist

	with open('words_alpha.txt', 'r') as f:
		wordList = f.read().splitlines()

	#Make list with max 9 letter words

	maxNineLetterWordList = [w for w in wordList if len(w) < 10]

	#Make subList from words starting with each of the inputLetters
	subList = []
	for letter in inputLetters:
		x = [w for w in maxNineLetterWordList if w.startswith(letter)]
		subList = subList + x


	# check if 
	haveLettersList = []
	for word in subList:
		should_include = True
		for excluded_letter in notInputLetters:
			if excluded_letter in word:
				should_include = False
		if should_include:
			haveLettersList.append(word) 		

	#Make letterScore for each letter in inputLetters

	inputLetterScore = dict((x, inputLetters.count(x)) for x in set(inputLetters))

	finalList = []
	for word in haveLettersList:
		wordListed = list(word)
		wordScore = dict((y, wordListed.count(y)) for y in set(wordListed))
		# parsedInputLetterScore = []
		if all(inputLetterScore[k] == wordScore[k] for k in wordScore):
			finalList.append(word)

	finalList = set(finalList)

	print("Here are all the 9 letter words: ")
	longest = ''
	for w in finalList: 
		if len(w) > len(longest):
			longest = w
	print(longest)

	return str(inputLetters) + str(longest) 
	
if __name__ == '__main__':
    app.run(port=5003, host='0.0.0.0', debug=True) 
