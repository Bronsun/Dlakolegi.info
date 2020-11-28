from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)


app.config['SECRET_KEY']='adsadsd3123kjhg32131iplksa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


from neuro.LinkConverterBasic.routes import LinkConvBasic
from neuro.Main.routes import Main
from neuro.Generator.routes import Generator
from neuro.Link.routes import Link

app.register_blueprint(Link)
app.register_blueprint(LinkConvBasic)
app.register_blueprint(Main)
app.register_blueprint(Generator)
