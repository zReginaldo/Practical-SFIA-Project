from flask import Flask, request, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import SubmitField
import wtforms.validators
import requests
from os import getenv

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')



let = ('http://51.104.32.215:5003/Letters')
nums = ('http://51.104.32.215:5003/Numbers')
 
class LettersRound(FlaskForm): 
    Restart = SubmitField('Start Again')


@app.route('/')
@app.route ('/lettersround', methods=['GET','POST'])
def LettRund(): 
    formR = LettersRound()
    Full = str(requests.get(let).text)
    Letters = Full[0:45]
    Longst_Wrd = Full[45:]


    return render_template('lettersround.html', Longst_Wrd=Longst_Wrd, Letters=Letters, formR=formR)


@app.route ('/numbersround', methods=['GET','POST'])
def NumRund(): 

    Fulls = str(requests.get(nums).text)
    formR = LettersRound() 
    snums = Fulls[12:24]
    lnums =Fulls[3:11]
    target = Fulls[0:3]
    calc = Fulls[25:-1]

    return render_template('numbersround.html', snums=snums,lnums=lnums, formR=formR, target=target, calc=calc)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)