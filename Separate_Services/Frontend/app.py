from flask import Flask, request, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import SubmitField
import wtforms.validators
import requests
from os import getenv

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')


class SubmitButton(FlaskForm): 
    Submit = SubmitField()


@app.route('/')
@app.route ('/Generate', methods=['GET','POST'])
def Generate(): 
    form = SubmitButton()
    Submit = str(requests.get('http://backend:5003/Prizegen').text)
    return render_template('index.html', form=form, Submit=Submit)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')