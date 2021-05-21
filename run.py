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
    
    sales_data = data_str.split(",")
    validate_data(sales_data)

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int or if there isn't exactly 6 values
    """
    print(values)
    try:
        if len(values) != 6:
            raise ValueError(
            f"Exactly 6 values provided, you only provide {len(values)}"
            )
    # Here we will except ValueError as e: The ValueError class here contains the details of the error triggered by the code in our  try statement here, 
    # and by using the as keyword, we're assigning that ValueError object to the e variable, which is standard Python shorthand for “error”.
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")

get_sales_data()


