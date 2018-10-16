import sqlite3

class Database:

    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS ITinventory (computername text)")
        self.conn.commit()
        #conn.close()

    def insert(self,title,author,year,isbn):
        self.cur.execute(" INSERT INTO ITinventory VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()
        #conn.close()

    def view(self):
        self.cur.execute(" SELECT * FROM 'Computer Name' ")
        rows=self.cur.fetchall()
        #self.conn.close()
        return rows

    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute(" SELECT * FROM ITinventory WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows=self.cur.fetchall()
        # conn.close()
        return rows

    def delete(self,id):
        self.cur.execute(" DELETE FROM ITinventory WHERE id=? ",(id,))
        self.conn.commit()
        #conn.close()

    def update(self,id,title,author,year,isbn):
        self.cur.execute(" UPDATE ITinventory SET title=?, author=?, year=?, isbn=? WHERE id=? ",(title,author,year,isbn,id))
        self.conn.commit()
        #conn.close()

    def __delete__(self):
        self.conn.close()



#connect()
#insert("The Earth","John Smith",1918,123912090234)
#delete(3)
#update(4,"The moon","John Smooth",1917,909090909)
#print(view())
#print(search(author="John Smith"))
