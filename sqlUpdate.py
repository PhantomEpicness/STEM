import MySQLdb
db = MySQLdb.connect(host = "localhost",user = "user",passwd="password",
db="school")
print("Hello World!")
#cursor

cur = db.cursor(MySQLdb.cursors.DictCursor)

sql = "UPDATE students SET gradeLvl=9 WHERE id=4)" # "SELECT * from students ORDER BY name"

cur.execute(sql)
rows = cur.fetchall()
#send code
db.autocommit(True)
cur.close()
db.close()
