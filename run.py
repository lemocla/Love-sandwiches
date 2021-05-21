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
    Get sales figures input from the user
    Run a while loop to collect valid string of data from the user
    via the terminal, which must be 6 numbers seperated by commas.
    The loop will request data repeatedly until valid. 
    """
    while True:
        print("Enter sales data from the last market.")
        print("Data should be 6 numbers, separated by commas.")
        print("Example: 10, 20, 30, 40, 50, 60 \n")

        data_str = input("Enter your data here: ")
    
        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid")
            break

    return sales_data

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int or if there isn't exactly 6 values
    """
    try:
        #list comprehension
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values provided, you provided {len(values)}"
            )
    # Here we will except ValueError as e: The ValueError class here contains the details of the error triggered by the code in our  try statement here, 
    # and by using the as keyword, we're assigning that ValueError object to the e variable, which is standard Python shorthand for “error”.
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with data list provided 
    """
    print("Updating sales worksheet ... \n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully \n")

data = get_sales_data()
sales_data = [int(num) for num in data]
update_sales_worksheet(sales_data)

# python3
# >>> enter code / not running run.py --> but code entered
# exit() to exit console
