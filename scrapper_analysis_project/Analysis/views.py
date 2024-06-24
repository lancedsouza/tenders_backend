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
#     head=df.head()

    
   

#     return render_template('rawdata.html',df=df)

