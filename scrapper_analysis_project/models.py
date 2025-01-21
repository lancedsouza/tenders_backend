from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from scrapper_analysis_project import db

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


class Product_name(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    product_name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(200), nullable=True)
    gem_id=db.Column(db.Integer,nullable=False)


