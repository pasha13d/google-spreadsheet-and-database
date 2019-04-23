import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name(
    './gsheet-credential.json', scope)
client = gspread.authorize(creds)
sheet = client.open('Search_Link').get_worksheet(0)
ROC_TSD = sheet.get_all_values()
print(ROC_TSD)

# import gspread
# import json
# import pprint
# import pyodbc
# from oauth2client.service_account import ServiceAccountCredentials

# scope = [
#     'https://spreadsheets.google.com/feeds',
#     'https://www.googleapis.com/auth/drive'
# ]
# creds = ServiceAccountCredentials.from_json_keyfile_name(
#     './testRead-65e52143bb68.json', scope)
# client = gspread.authorize(creds)
# sheet = client.open('Search_Link').get_worksheet(0)
# pp = pprint.PrettyPrinter()
# result = sheet.get_all_values()
# pp.pprint(result)

#DB Connection
# def read(conn):
#     print("Read")
#     cursor = conn.cursor()
#     cursor.execute("select * from dbo.Authors")
#     for row in cursor:
#         print('row = %r' % (row,))
#     print()
# conn = pyodbc.connect("Driver = {SQL Server Native Client 11.0};"
#                       "Server = MAHABUB;"
#                       "Database = Pluto;"
#                       "Trusted_Connection = yes;")

# read(conn)
# conn.close()