from flask import Blueprint,render_template,redirect,url_for,flash,request
from flask import Flask, send_file, render_template, make_response
from flask import get_flashed_messages
from sqlalchemy import func
# from my_project.purchase_order.forms import InforForm
from sqlalchemy import insert 
from scrapper_analysis_project import db
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import plotly.express as px

from google.oauth2 import service_account
from googleapiclient.discovery import build


from flask import render_template, request
from google.oauth2 import service_account
from googleapiclient.discovery import build
import pandas as pd
import io

# Authenticate and create a PyDrive client

from oauth2client.service_account import ServiceAccountCredentials

from  scrapper_analysis_project.models import Product
from datetime import datetime, timedelta
import pytesseract
from PIL import Image
import io
import base64



product_name_blueprint=Blueprint('product_name',__name__,template_folder='/templates/scraper.html')
analyze_data_blueprint=Blueprint('analyze_data',__name__,template_folder='templates/Scrapper')
analyze_data1_blueprint=Blueprint('analyze_data1',__name__,template_folder='templates/Scrapper')
analyze_data2_blueprint=Blueprint('analyze_data2',__name__,template_folder='templates/Scrapper')
analyze_data3_blueprint=Blueprint('analyze_data3',__name__,template_folder='templates/Scrapper')
analyze_data4_blueprint=Blueprint('analyze_data4',__name__,template_folder='templates/Scrapper')


import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import os
import base64
import time
import io
from PIL import Image
import pytesseract
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import openpyxl




# @product_name_blueprint.route('/product_name', methods=['GET', 'POST'])
# def product_name():
#     if request.method == "POST":
#         products_name = request.form.get('product_name')
#         month = request.form.get('month_from')
#         year = request.form.get('year_from')

#         # Start a Chrome WebDriver instance
#         # Function to solve CAPTCHA
# def solve_captcha(image_base64):
#     image_data = base64.b64decode(image_base64)
#     image = Image.open(io.BytesIO(image_data))
#     captcha_solution = pytesseract.image_to_string(image)
#     return captcha_solution.strip()
    

# # Start a Chrome WebDriver instance
# chrome_options = Options()
# chrome_options.add_argument("--disable-notifications")
# driver = webdriver.Chrome(options=chrome_options)
# driver.maximize_window()

# try:
#     # Navigate to the target website
#     website = 'https://gem.gov.in/view_contracts'
#     driver.get(website)

#     # Handling drop down in the Category option
#     products_name = "Example Category"  # Replace with actual category
#     dropdown_category = Select(driver.find_element(By.ID, 'buyer_category'))
#     dropdown_category.select_by_visible_text(products_name)
#     time.sleep(3)

#     # Handling Contract Date From
#     # Click on the input field to activate the calendar
#     date_input = driver.find_element(By.ID, 'from_date_contract_search1')
#     date_input.click()

#     # Selecting the month (assuming you want to select January)

#     year_dropdown = Select(driver.find_element(By.CSS_SELECTOR, 'select.ui-datepicker-year'))
#     year_dropdown.select_by_visible_text(str(year))

#     month_dropdown = Select(driver.find_element(By.CSS_SELECTOR, 'select.ui-datepicker-month'))
#     month_dropdown.select_by_visible_text(str(month))
#     # Click on the date (assuming you want to select the 1st of January)
#     date_element = driver.find_element(By.XPATH, '//a[text()="1"]')
#     date_element.click()
    
#     # Handling CAPTCHA
#     time.sleep(3)
#     captcha_image = driver.find_element(By.ID, 'captchaimg1').get_attribute('src').split(",")[1]
#     captcha_solution = solve_captcha(captcha_image)
#     captcha_input = driver.find_element(By.ID, 'captcha_code1')
#     captcha_input.send_keys(captcha_solution)

#     time.sleep(5)
#     # Submit the form (adjust the form submission part as per your requirement)
#     submit_button = driver.find_element(By.ID, 'searchlocation1')  # Adjust this to the actual submit button's ID
#     submit_button.click()

#     # Data extraction lists
#     contract_number = []
#     organization_type = []
#     Ministry = []
#     Department = []
#     Organization_name = []
#     office_zone = []
#     Buyer_Designation = []
#     buying_mode = []
#     contract_date = []
#     Total = []
#     products = []
#     brands = []
#     models = []
#     Quantities = []
#     Prices = []

#     # Get the initial height of the page
#     last_height = driver.execute_script("return document.body.scrollHeight")

#     while True:
#         # Scroll down to the bottom
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(10)  # Adjust the sleep time as needed

#         # Wait to load page
#         #
#         time.sleep(6)  # You can adjust this value as needed

#         # Calculate new scroll height and compare with last scroll height
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#             break
#         last_height = new_height

#     # Extracting all containers
#     all_containers = driver.find_elements(By.ID, 'pagi_content')

#     # Extracting info from each container
#     for container in all_containers:
#         try:
#             contract_no = container.find_elements(By.CLASS_NAME, 'ajxtag_order_number')
#             for contract in contract_no:
#                 contract_number.append(contract.text)
#         except NoSuchElementException:
#             contract_number.append("N/A")

#         try:
#             org_type = container.find_elements(By.XPATH, '//p/strong[text()="Organization Type: "]/following-sibling::span[@class="ajxtag_buyer_dept_org"]')
#             for org in org_type:
#                 organization_type.append(org.text)
#         except NoSuchElementException:
#             organization_type.append("N/A")

#         try:
#             ministry = container.find_elements(By.XPATH, '//p/strong[text()="Ministry: "]/following-sibling::span[@class="ajxtag_buying_mode"]')
#             for ele in ministry:
#                 Ministry.append(ele.text)
#         except NoSuchElementException:
#             Ministry.append("N/A")

#         try:
#             department = container.find_elements(By.XPATH, '//p/strong[text()="Department: "]/following-sibling::span[@class="ajxtag_buying_mode"]')
#             for dept in department:
#                 Department.append(dept.text)
#         except NoSuchElementException:
#             Department.append("N/A")

#         try:
#             org_name = container.find_elements(By.XPATH, '//p/strong[text()="Organization Name: "]/following-sibling::span[@class="ajxtag_buyer_dept_org"]')
#             for org in org_name:
#                 Organization_name.append(org.text)
#         except NoSuchElementException:
#             Organization_name.append("N/A")

#         try:
#             off_zone = container.find_elements(By.XPATH, '//p/strong[text()="Office Zone: "]/following-sibling::span[@class="ajxtag_buying_mode"]')
#             for zone in off_zone:
#                 office_zone.append(zone.text)
#         except NoSuchElementException:
#             office_zone.append("N/A")

#         try:
#             buyer_designation_element = container.find_elements(By.XPATH, '//p/strong[text()="Buyer Designation: "]/following-sibling::span[@class="ajxtag_buyer_dept_org"]')
#             for designation in buyer_designation_element:
#                 Buyer_Designation.append(designation.text)
#         except NoSuchElementException:
#             Buyer_Designation.append("N/A")

#         try:
#             buy_mode = container.find_elements(By.XPATH, '//p/strong[text()="Buying Mode: "]/following-sibling::span[@class="ajxtag_buying_mode"]')
#             for mode in buy_mode:
#                 buying_mode.append(mode.text)
#         except NoSuchElementException:
#             buying_mode.append("N/A")

#         try:
#             contr_date = container.find_elements(By.XPATH, '//p/strong[text()="Contract Date: "]/following-sibling::span[@class="ajxtag_contract_date"]')
#             for date in contr_date:
#                 contract_date.append(date.text)
#         except NoSuchElementException:
#             contract_date.append("N/A")

#         try:
#             total = container.find_elements(By.XPATH, '//p/strong[text()="Total: "]/following-sibling::span[@class="ajxtag_totalvalue"]')
#             for value in total:
#                 Total.append(value.text)
#         except NoSuchElementException:
#             Total.append("N/A")

#         try:
#             prods = container.find_elements(By.XPATH, './/table/tbody/tr[2]/td[1]')
#             for prod in prods:
#                 products.append(prod.text)
#         except NoSuchElementException:
#             products.append("N/A")

#         try:
#             brand_ = container.find_elements(By.XPATH, './/table/tbody/tr[2]/td[2]')
#             for brand in brand_:
#                 brands.append(brand.text)
#         except NoSuchElementException:
#             brands.append("N/A")

#         try:
#             model_ = container.find_elements(By.XPATH, './/table/tbody/tr[2]/td[3]')
#             for model in model_:
#                 models.append(model.text)
#         except NoSuchElementException:
#             models.append("N/A")

#         try:
#             quantity_ = container.find_elements(By.XPATH, './/table/tbody/tr[2]/td[4]')
#             for quantity in quantity_:
#                 Quantities.append(quantity.text)
#         except NoSuchElementException:
#             Quantities.append("N/A")

#         try:
#             price_ = container.find_elements(By.XPATH, './/table/tbody/tr[2]/td[5]')
#             for price in price_:
#                 Prices.append(price.text)
#         except NoSuchElementException:
#             Prices.append("N/A")

    
#     # Create DataFrame
#     products_data = []
#     for i in range(len(contract_number)):
#         produc = Product(
#         Contract_Number=contract_number[i],
#         Organization_Type=organization_type[i],
#         Ministry=Ministry[i],
#         Department=Department[i],
#         Organization_Name=Organization_name[i],
#         Office_Zone=office_zone[i],
#         Buyer_Designation=Buyer_Designation[i],
#         Buying_Mode=buying_mode[i],
#         Contract_Date=datetime.strptime(contract_date[i], '%Y-%m-%d'),  # Convert string to datetime
#         Total=float(Total[i]),  # Convert string to float
#         Product=products[i],
#         Brands=brands[i],
#         Models=models[i],
#         Quantities=int(Quantities[i]),  # Convert string to int
#         Prices=Prices[i]
#     )
#     products_data.append(produc)
#     try:
#         # Add products_data to the database session
#         db.session.add_all(products_data)

#         # Commit the changes to the database
#         db.session.commit()

#     except Exception as e:
#         db.session.rollback()  # Rollback changes in case of an exception
#         print(f"Error occurred: {str(e)}")
#         # Handle the exception as needed (logging, notifying, etc.)

# finally:
#     db.session.close()  # Close the session to release resources
    



# @analyze_data_blueprint.route('/analyze_data',methods=['POST', 'GET'])
# def analyze_data():
#     import os
#     import pandas as pd

#     # Define the path to the data file
#     file_name = 'Amit_Rapid_Test_ Kits.xlsx'  # Adjusted file name with space
#     # Specify the correct directory where the file is located
#     file_path = os.path.join('C:\\Users\\Wishes Lawrence', file_name)

#     # Load the data from the Excel file
#     df = pd.read_excel(file_path)
#     df1=df.head(5)  

#     stats=df.describe()

#     return render_template('rawdata.html',df=df1)
import logging
from google.oauth2 import service_account
from googleapiclient.discovery import build
import pandas as pd
import os
from flask import render_template, request
import io
import requests
from googleapiclient.errors import HttpError  # Import HttpError
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from PIL import Image

# from io import BytesIO

# import asyncio
# from flask import Flask, render_template, jsonify
# from google.oauth2 import service_account
# from googleapiclient.discovery import build
# import pandas as pd

# app = Flask(__name__)

# # Path to service account credentials and Google Sheets file ID
# credentials_file = credentials_file = 'C:\\Users\\Wishes Lawrence\\Desktop\\lace-data1\\Desktop\\Scrapper_app\\gemportal-bacb7ef8a2f8.json'
# file_id = 'your_google_sheets_file_id'
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# # Example async function to fetch data from Google Sheets
# async def fetch_google_sheets_data():
#     credentials = service_account.Credentials.from_service_account_file(credentials_file, scopes=SCOPES)
#     sheets_service = build('sheets', 'v4', credentials=credentials)
#     result = sheets_service.spreadsheets().values().get(spreadsheetId=file_id, range='Sheet1').execute()
#     values = result.get('values', [])
#     return values

# # Example async function to process data
# async def process_data():
#     data = await fetch_google_sheets_data()
#     df = pd.DataFrame(data[1:], columns=data[0])
#     # Perform data processing as needed
#     return df

# # Route to asynchronously fetch and process data
# @app.route('/async-data')
# async def async_data():
#     try:
#         df = await process_data()
#         # Example: Convert DataFrame to JSON for API response
#         data_json = df.to_json()
#         return jsonify({'data': data_json})
#     except Exception as e:
#         return jsonify({'error': str(e)})



# # Path to your service account key file
# credentials_file = 'C:\\Users\\Wishes Lawrence\\Desktop\\lace-data1\\Desktop\\Scrapper_app\\gemportal-bacb7ef8a2f8.json'

# # ID of the Google Sheets file you want to access
# file_id = '1nlO1cw0j0JCjRo2yg08B8jqh7RIv9scGCVUYiXePN6c'

# # Define the scopes for the Sheets API
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# @analyze_data_blueprint.route('/analyze_data', methods=['GET'])
# def analyze_data():
#     try:
#         # Authenticate using service account credentials
#         credentials = service_account.Credentials.from_service_account_file(credentials_file, scopes=SCOPES)

#         # Build the Sheets API service
#         sheets_service = build('sheets', 'v4', credentials=credentials)

#         # Specify the range of data you want to retrieve from the spreadsheet
#         range_name =  'Sheet1!A1:O615'  # Adjust based on your actual data range

#         # Retrieve data from Google Sheets
#         sheet = sheets_service.spreadsheets()
#         result = sheets_service.spreadsheets().values().get(spreadsheetId=file_id, range='Sheet1').execute()
#         values = result.get('values', [])

#         if not values:
#             print('No data found.')

#         # Convert the data to a Pandas DataFrame or process it as needed
#         # Example: Convert to HTML for rendering in a template
#         df = pd.DataFrame(values[1:], columns=values[0])
#         # Process the DataFrame as needed (example: get head and descriptive stats)
#         head = df.head()
#         stats = df.describe()

#         # Convert DataFrame objects to HTML tables
#         head_html = head.to_html(classes='table table-striped', index=False)
#         stats_html = stats.to_html(classes='table table-striped')

#         # Render HTML template with DataFrame tables
#         return render_template('rawdata.html', head_html=head_html, stats_html=stats_html)
#     except Exception as e:
#         print(f'Error accessing or processing Google Sheets file: {e}')
#         return f'Error accessing or processing Google Sheets file: {e}'

# Define authentication credentials and file ID for Google Sheets
credentials_file = 'C:\\Users\\Wishes Lawrence\\Desktop\\lace-data1\\Desktop\\Scrapper_app\\gemportal-cafdf2c8cc08.json'

file_id = '1nlO1cw0j0JCjRo2yg08B8jqh7RIv9scGCVUYiXePN6c'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# Define asynchronous function to fetch data from Google Sheets
@analyze_data_blueprint.route('/analyze_data', methods=['GET'])
async def analyze_data():
    try:
        credentials = service_account.Credentials.from_service_account_file(credentials_file, scopes=SCOPES)
        sheets_service = build('sheets', 'v4', credentials=credentials)
        
        # Fetch data from Google Sheets
        result = sheets_service.spreadsheets().values().get(spreadsheetId=file_id, range='Sheet1').execute()
        values = result.get('values', [])
        
        # Process data into Pandas DataFrame
        df = pd.DataFrame(values[1:], columns=values[0])
        # Process the DataFrame as needed (example: get head and descriptive stats)
        head = df.head()
        stats = df.describe()

        # Convert DataFrame objects to HTML tables
        head_html = head.to_html(classes='table table-striped', index=False)
        stats_html = stats.to_html(classes='table table-striped')

        # Render HTML template with DataFrame tables
        return render_template('rawdata.html', head_html=head_html, stats_html=stats_html)
    except Exception as e:
        print(f'Error accessing or processing Google Sheets file: {e}')
        return f'Error accessing or processing Google Sheets file: {e}'
      


    
@analyze_data1_blueprint.route('/analyze_data1', methods=['POST', 'GET'])
def analyze_data1():
    plt.ioff()
    credentials = service_account.Credentials.from_service_account_file(credentials_file, scopes=SCOPES)

        # Build the Sheets API service
    sheets_service = build('sheets', 'v4', credentials=credentials)

    # Specify the range of data you want to retrieve from the spreadsheet
    # range_name =  'Sheet1!A1:O615'  # Adjust based on your actual data range

    # Retrieve data from Google Sheets
    sheet = sheets_service.spreadsheets()
    result = sheets_service.spreadsheets().values().get(spreadsheetId=file_id, range='Sheet1').execute()
    values = result.get('values', [])
    
        # Matplotlib plot generation
    # file_name = 'Amit_Rapid_Test_ Kits.xlsx'  # Adjusted file name with space
    # file_path = os.path.join('C:\\Users\\Wishes Lawrence', file_name)
    df = pd.DataFrame(values[1:], columns=values[0])
  # Assuming df is your DataFrame and it has a column named 'Organization_name'
    org_name = df['organization_type'].value_counts().head(10)
    x = org_name.index
    y = org_name.values

    # Create the bar plot using Plotly Express
    fig = px.bar(x=x, y=y, labels={'x': 'Organization Name', 'y': 'Count'}, title='Top 10 Organization Names by Count')

    # Save the plot to a BytesIO object
    img = io.BytesIO()
    fig.write_image(img, format='png')
    img.seek(0)

        # Serve the image as a response
    return send_file(img, mimetype='image/png')

@analyze_data2_blueprint.route('/analyze_data2', methods=['POST', 'GET'])
def analyze_data2():
    plt.ioff()
    credentials = service_account.Credentials.from_service_account_file(credentials_file, scopes=SCOPES)

        # Build the Sheets API service
    sheets_service = build('sheets', 'v4', credentials=credentials)

    # Specify the range of data you want to retrieve from the spreadsheet
    # range_name =  'Sheet1!A1:O615'  # Adjust based on your actual data range

    # Retrieve data from Google Sheets
    sheet = sheets_service.spreadsheets()
    result = sheets_service.spreadsheets().values().get(spreadsheetId=file_id, range='Sheet1').execute()
    values = result.get('values', [])
    
        # Matplotlib plot generation
    # file_name = 'Amit_Rapid_Test_ Kits.xlsx'  # Adjusted file name with space
    # file_path = os.path.join('C:\\Users\\Wishes Lawrence', file_name)
    df = pd.DataFrame(values[1:], columns=values[0])

    org_name = df['organization_type'].value_counts().head(10)  # Select the top 10
    x = org_name.index
    y = org_name.values
    # declaring data 
    data = org_name.values
    keys = org_name.index
    plt.rcParams["figure.figsize"] = (10,5)
    fig, ax = plt.subplots()
    # define Seaborn color palette to use 
    palette_color = sns.color_palette('bright') 
    explode = (0.1, 0, 0, 0,0,0,0,0,0)
    wedges, texts, autotexts = ax.pie(data, autopct='%1.1f%%',pctdistance=0.8,labeldistance=4,explode=explode,
                                textprops=dict(color="black", fontsize=8, fontweight="bold"))  
    ax.legend(wedges, keys,
            title="Organizations",
            loc="center left",
            bbox_to_anchor=(1, 0.5, 0.5, 1))
    img1 = io.BytesIO()
    plt.savefig(img1, format='png')
    img1.seek(0)

    # Optionally, clear the plot from memory
    plt.clf()
    plt.close(fig)  # Close the figure to free memory

    # Serve the image as a response
    return send_file(img1, mimetype='image/png')
    
    
    # plotting data on chart 
    # plt.pie(data, labels=keys, colors=palette_color, labeldistance=3,autopct='%.0f%%') 

@analyze_data3_blueprint.route('/analyze_data3', methods=['POST', 'GET'])
def analyze_data3():
    # Assuming you have fetched data and stored it in the DataFrame df
    plt.ioff()
    credentials = service_account.Credentials.from_service_account_file(credentials_file, scopes=SCOPES)

        # Build the Sheets API service
    sheets_service = build('sheets', 'v4', credentials=credentials)

    # Specify the range of data you want to retrieve from the spreadsheet
    # range_name =  'Sheet1!A1:O615'  # Adjust based on your actual data range

    # Retrieve data from Google Sheets
    sheet = sheets_service.spreadsheets()
    result = sheets_service.spreadsheets().values().get(spreadsheetId=file_id, range='Sheet1').execute()
    values = result.get('values', [])
    
        # Matplotlib plot generation
    # file_name = 'Amit_Rapid_Test_ Kits.xlsx'  # Adjusted file name with space
    # file_path = os.path.join('C:\\Users\\Wishes Lawrence', file_name)
    df = pd.DataFrame(values[1:], columns=values[0])
  
   

    fig = px.scatter(df, x=df['Total'], y=df['Quantities'],color='Total',hover_data=['Quantities'])

    # Convert the plot to a BytesIO object
    img2 = io.BytesIO()
    fig.write_image(img2, format='png', engine='kaleido')  # Specify engine as 'kaleido'
    img2.seek(0)

    # Optionally, clear the figure from memory
    fig = None

    # Serve the image as a response
    return send_file(img2, mimetype='image/png')


@analyze_data4_blueprint.route('/analyze_data4', methods=['POST', 'GET'])
def analyze_data4():
    plt.ioff()
    credentials = service_account.Credentials.from_service_account_file(credentials_file, scopes=SCOPES)

        # Build the Sheets API service
    sheets_service = build('sheets', 'v4', credentials=credentials)

    # Specify the range of data you want to retrieve from the spreadsheet
    # range_name =  'Sheet1!A1:O615'  # Adjust based on your actual data range

    # Retrieve data from Google Sheets
    sheet = sheets_service.spreadsheets()
    result = sheets_service.spreadsheets().values().get(spreadsheetId=file_id, range='Sheet1').execute()
    values = result.get('values', [])
    
        # Matplotlib plot generation
    # file_name = 'Amit_Rapid_Test_ Kits.xlsx'  # Adjusted file name with space
    # file_path = os.path.join('C:\\Users\\Wishes Lawrence', file_name)
    df = pd.DataFrame(values[1:], columns=values[0])
  # Assuming df is your DataFrame and it has a column named 'Organization_name'
    # Calculate the value counts
    brand_counts = df['brands'].value_counts().head(10)

# Create a DataFrame for plotting
    plot_data = pd.DataFrame({
    'Organization Name': brand_counts.index,
    'Count': brand_counts.values
})

# Create the bar plot using Plotly Express with a color sequence
    fig = px.bar(plot_data, 
             x='Count', 
             y='Organization Name', 
             orientation='h', 
             labels={'Count': 'Count', 'Organization Name': 'Organization Name'},
             title='Top 10 Organization Names by Count',
             color='Organization Name',  # Use organization names as the color category
             color_discrete_sequence=px.colors.qualitative.Pastel  # Use a predefined color sequence
            )
# Save the plot to a BytesIO object
    img3 = io.BytesIO()
    fig.write_image(img3, format='png')
    img3.seek(0)

        # Serve the image as a response
    return send_file(img3, mimetype='image/png')