import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER,price REAL)")
    #cur.execute(" INSERT INTO store VALUES ('Wine Glass',8,10.5)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432' ")
    cur = conn.cursor()
    # cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER,price REAL)")
    # cur.execute(" INSERT INTO store VALUES ('Wine Glass',8,10.5)")
    # cur.execute(" INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    # work well but injection SQLcur.execute(" INSERT INTO store VALUES ('%s', '%s' , '%s')" %(item,quantity,price))
    cur.execute(" INSERT INTO store VALUES (%s,%s,%s)", %(item,quantity,price))
    conn.commit()
    conn.close()

# insert('Wine Glass',8,10.5)

def view():
    conn = psycopg2.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item= ?",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn = psycopg2.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price= ? WHERE item = ?",(quantity,price,item))
    conn.commit()
    conn.close()

create_table()
insert("Apple",10,15)
#update(11,6,"Wine Glass")
# delete("Wine Glass")
#print(view())
#insert('Wine Glass',10,5)
