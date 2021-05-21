# Import google auth library
import gspread
from google.oauth2.service_account import Credentials

# The scope lists the APIs that the  program should access in order to run.
# Constant are in capitals
SCOPE = [   
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Call the from_service_account_file  method of the Credentials class  
CREDS = Credentials.from_service_account_file('creds.json')

# Now our scope and creds variables  are ready, we’ll create a new variable
# Use the  with_scopes method of the creds object
SCOPED_CREDS = CREDS.with_scopes(SCOPE)

# Using the gspread authorize method,  and pass it our SCOPED_CREDS.
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Open spreadsheet 
SHEET = GSPREAD_CLIENT.open("love_sandwiches")

# Run code in terminal python3 run.py 

def get_sales_data():
    """
    get sales figures input from the user
    """
    print("Enter sales data from the last market.")
    print("Data should be 6 numbers, separated by commas.")
    print("Example: 10, 20, 30, 40, 50, 60 \n")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")

get_sales_data()
