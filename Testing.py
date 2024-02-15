import sqlite3 as s

con=s.connect('mukesh.db')
cur=con.cursor()

with open('./industry.csv','r+') as csvfile:
    f=csvfile.readlines()

print(f)
for line in f:
    print(line)
    cur.execute('insert into  industries values (?)', ((line,))
#cur.executemany("insert into  industries values (?)", (f,))
con.commit()

