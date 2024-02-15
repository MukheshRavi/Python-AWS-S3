import sqlite3 as s

con=s.connect('mukesh.db')
cur=con.cursor()
#cur.execute('create table industries(industry)')
res=cur.execute('select * from industries')
#con.commit()
print(res.fetchall())
