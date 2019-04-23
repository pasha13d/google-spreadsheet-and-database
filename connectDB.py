import pyodbc

# def read(conn):
#     print("Read")
#     cursor = conn.cursor()
#     cursor.execute("select * from dbo.Authors")
#     cursor.fetchall()
#     for row in cursor:
#         print('row = %r' % (row,))
#     print()
conn = pyodbc.connect(
    Trusted_Connection='Yes',
    Driver='{SQL Server Native Client 11.0}',
    Server='MAHABUB',
    Database='Pluto',
    username='sa',
    password='Password_1')
cur = conn.cursor()
cur.execute("select * from dbo.Authors")
for row in cur:
    print(row.Name)
cur.close()
conn.close()