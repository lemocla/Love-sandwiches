# Import google auth library 
import gspread
from google.oauth2.service_account import Credentials

# The scope lists the APIs that the  program should access in order to run.
SCOPE = [ # Constant are in capitals
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Call the from_service_account_file  method of the Credentials class,  
CREDS = Credentials.from_service_account_file('creds.json')

# Now our scope and creds variables  are ready, we’ll create a new variable, 
# Use the  with_scopes method of the creds object,  
SCOPED_CREDS = CREDS.with_scopes(SCOPE) 

#Using the gspread authorize method,  and pass it our SCOPED_CREDS.
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

#Open spreadsheet 
SHEET = GSPREAD_CLIENT.open("love_sandwiches")

sales = SHEET.worksheet("sales")
data = sales.get_all_values()
#Run code in terminal python3 run.py 
print(data)

