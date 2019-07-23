from app import app
from flask import render_template, request, redirect

def stone(form_answer):
    if form_answer.capitalize == "January":
        return "Your birthstone is Garnet"
    elif form_answer.capitalize == "February":
        return "Your birthstone is Amethyst"
    elif form_answer.capitalize == "March":
        return "Your birthstone is Aquamarine"
    elif form_answer.capitalize == "April":
        return "Your birthstone is Diamond"
    elif form_answer.capitalize == "May":
        return "Your birthstone is Emerald"
    elif form_answer.capitalize == "June":
        return "Your birthstone is Pearl"
    elif form_answer.capitalize == "July":
        return "Your birthstone is Ruby"
    elif form_answer.capitalize == "August":
        return "Your birthstone is Peridot"
    elif form_answer.capitalize == "September":
        return "Your birthstone is Sapphire"
    elif form_answer.capitalize == "October":
        return "Your birthstone is Opal"
    elif form_answer.capitalize() == "November":
        return "Your birthstone is Topaz"
    elif form_answer.capitalize == "December":
        return "Your birthstone is Turquoise"
    
    