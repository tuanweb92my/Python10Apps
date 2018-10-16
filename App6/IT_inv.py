import sqlite3
import pandas as pd
filename="IT_inven"
con=sqlite3.connect(filename+".db")
wb=pd.read_excel(filename+'.xls',sheetname='computername')
for sheet in wb:
    wb[sheet].to_sql(sheet,con, index=False)
con.commit()
con.close()
