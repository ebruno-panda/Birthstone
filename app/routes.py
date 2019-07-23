from app import app
from flask import render_template, request, redirect
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

def results():
    return render_template('results.html')
    
    
@app.route('/birthday', methods = ['GET', 'POST'])
def birthday_stone():
    if request.method =="GET":
        return"You're a loser"
    else:
        user_data = request.form
        print(user_data)
        month = user_data["Birth Month"]
        birth_sentence = model.stone(month)
        print(birth_sentence)
        # return birth_sentence
        
        return render_template('results.html', birth_sentence=birth_sentence)
        
        # return(user_data)

