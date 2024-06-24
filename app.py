from scrapper_analysis_project import app
from flask import render_template
from scrapper_analysis_project import db


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')  # New route for displaying the home page
def home():
    return render_template('home.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables based on your models

    app.run(debug=True)
