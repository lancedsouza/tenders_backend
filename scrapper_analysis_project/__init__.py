import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from google.oauth2 import service_account
from googleapiclient.discovery import build
from flask_cors import CORS


app=Flask(__name__)
cors = CORS(app)  # Enable CORS for all origins
basedir=os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY']='hello'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'lance.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)
migrate = Migrate(app, db)
Migrate(app, db,render_as_batch=True)
# Import your blueprints from their respective locations
from scrapper_analysis_project.Scrapper.views import product_name_blueprint
from scrapper_analysis_project.Scrapper.views import analyze_data_blueprint
from scrapper_analysis_project.Scrapper.views import analyze_data1_blueprint
from scrapper_analysis_project.Scrapper.views import analyze_data2_blueprint
from scrapper_analysis_project.Scrapper.views import analyze_data3_blueprint
from scrapper_analysis_project.Scrapper.views import analyze_data4_blueprint

# Register your blueprints with the Flask app
app.register_blueprint(product_name_blueprint, url_prefix='/product_name')
app.register_blueprint(analyze_data_blueprint, url_prefix='/analyze_data')
app.register_blueprint(analyze_data1_blueprint, url_prefix='/analyze_data1')
app.register_blueprint(analyze_data2_blueprint, url_prefix='/analyze_data2')
app.register_blueprint(analyze_data3_blueprint, url_prefix='/analyze_data3')
app.register_blueprint(analyze_data4_blueprint, url_prefix='/analyze_data4')
