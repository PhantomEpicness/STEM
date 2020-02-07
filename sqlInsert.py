import MySQLdb
db = MySQLdb.connect(host = "192.168.0.131",user = "donwya21",passwd="wyand",
db="donwya21")
print("Hello World!")
#cursor

cur = db.cursor(MySQLdb.cursors.DictCursor)
sql = "INSERT INTO students (name,age,gradeLVL) VALUES ({'moment'},{3},{1})" # "SELECT * from students ORDER BY name"
cur.execute(sql)
rows = cur.fetchall()
age = 10
db.autocommit(True)
name = "bob"
for row in rows:
	print(row['name'] + " " + str(row['age']) + " " + str(row['gradeLVL']))
cur.close()
db.close()


