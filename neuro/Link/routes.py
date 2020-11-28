from flask import render_template, url_for, flash, redirect,request,Blueprint
from neuro import app,db
from neuro.modules import UserLink

Link = Blueprint('Link',__name__)

@Link.route('/links2881',methods=['GET','POST'])
def links():
    
    users = UserLink.query.all()

    return render_template('links.html',users=users)
@Link.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404