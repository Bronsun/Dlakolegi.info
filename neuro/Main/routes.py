from flask import render_template, url_for, flash, redirect,request,Blueprint
from neuro import app,db
from neuro.modules import UserLink

Main = Blueprint('Main',__name__)


@Main.route('/')
def index():
    error=None
       
    link=UserLink.query.count()+1482
    
    return render_template('main.html',link=link,error=error) 


@Main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404