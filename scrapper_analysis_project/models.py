from sqlalchemy import Column, Integer, ForeignKey, String, Float, Date
from sqlalchemy.orm import relationship
from scrapper_analysis_project import db
from werkzeug.security  import generate_password_hash,check_password_hash







    



class Product(db.Model):
    __tablename__ = 'product'

    Contract_Number = db.Column(db.Integer, primary_key=True, nullable=False)
    Organization_Type = db.Column(db.String(255), nullable=False)
    Ministry = db.Column(db.String(255), nullable=False)
    Department = db.Column(db.String(255), nullable=False)
    Organization_Name = db.Column(db.String(50), nullable=True)
    Office_Zone = db.Column(db.String(50), nullable=True)
    Buyer_Designation = db.Column(db.String(255), nullable=False)
    Buying_Mode = db.Column(db.String(255), nullable=False)
    Contract_Date = db.Column(db.Date, nullable=False)
    Total = db.Column(db.Float, nullable=False)
    Product = db.Column(db.String(255), nullable=False)
    Brands = db.Column(db.String(255), nullable=False)
    Models = db.Column(db.String(255), nullable=False)
    Quantities = db.Column(db.Integer, nullable=False)
    Prices = db.Column(db.String(255), nullable=False)
