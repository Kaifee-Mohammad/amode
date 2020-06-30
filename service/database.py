import pyodbc
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'localhost,1433'
database = 'amode'
username = 'amode'
password = 'amode'
# cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
#                       # UID='+username+';PWD=' + password)
#                       server+';DATABASE='+database+';Trusted_Connection=yes;')
cnxn = pyodbc.connect('DSN=dsn_amode;UID=amode;PWD=amode;')
cursor = cnxn.cursor()

# Sample select query
cursor.execute("SELECT * from batch;")
row = cursor.fetchone()
while row:
    print(row[1])
    row = cursor.fetchone()
