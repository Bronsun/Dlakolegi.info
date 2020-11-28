from flask import render_template, url_for, flash, redirect,request,Blueprint
from neuro import app,db
from neuro.modules import UserLink, Links
import pandas as pd


import random 

Generator = Blueprint('Generator',__name__)

@Generator.route('/gen', methods=['GET','POST'])
def gen():
    rand = int(random.randrange(1,100))
    link1 =Links.query.get(rand)
    return render_template('generator.html',link1=link1) 
    
