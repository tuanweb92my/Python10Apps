import os
import sqlite3
from win32com.client import constants, Dispatch

#----------------------------------------
# get data from excel file
#----------------------------------------
XLS_FILE = os.getcwd() + "\\IT_inven.xls"
ROW_SPAN = (14, 21)
COL_SPAN = (2, 7)
app = Dispatch("Excel.Application")
app.Visible = True
ws = app.Workbooks.Open(XLS_FILE).Sheets(1)
exceldata = [[ws.Cells(row, col).Value
              for col in xrange(COL_SPAN[0], COL_SPAN[1])]
             for row in xrange(ROW_SPAN[0], ROW_SPAN[1])]

#----------------------------------------
# create SQL table and fill it with data
#----------------------------------------
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE exceltable (
   computername TEXT,
   enduser TEXT,
   serial TEXT,
   model TEXT,
   lost TEXT,
   assetlist TEXT
)''')
for row in exceldata:
    c.execute('INSERT INTO exceltable VALUES (?,?,?,?,?)', row)
conn.commit()

#----------------------------------------
# display SQL data
#----------------------------------------
c.execute('SELECT * FROM exceltable')
for row in c:
    print(row)
