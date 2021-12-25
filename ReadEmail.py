from googleapiclient.discovery import build
from google.oauth2 import service_account
import time

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'readsheets-336107-690031a8e6b8.json'
global sheet_empty
global counter
sheet_empty = True
counter = 0

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1AQuq6dVX24Fid2ctuVRUNjaTN1uWxA0T3esDyVeby_k'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API until value found

while sheet_empty:
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='Form Responses 1!B2:B2').execute()
    values = result.get('values')

    if values is not None:
        sheet_empty = False
        print('Email obtained.')
    else:
        print('Standby ' + str(counter))
        print()
        counter += 1
    time.sleep(2)
