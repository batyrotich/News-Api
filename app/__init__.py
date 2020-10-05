from flask import Flask
from .config import DevConfig

app = Flask(__name__, instance_relative_config = True)

#setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#Initializing Flask Extensions
bootstrap = Bootsrap(app)


from app import views