import MySQLdb
db = MySQLdb.connect(host = "localhost",user = "username",passwd="password",
db="students")
print("Hello World!")
#cursor

cur = db.cursor(MySQLdb.cursors.DictCursor)
sql = "SELECT * FROM students" # "SELECT * from students ORDER BY name"
cur.execute(sql)
rows = cur.fetchall()
age = 10
db.autocommit(True)
name = "bob"
for row in rows:
	print(row['name'] + " " + str(row['age']) + " " + str(row['gradeLVL']))
cur.close()
db.close()
