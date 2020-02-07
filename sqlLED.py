import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(18,GPIO.OUT)

import MySQLdb

db = MySQLdb.connect(host = "localhost",user = "username",passwd="password",
db="students")
print("Hello World!")
#cursor

cur = db.cursor(MySQLdb.cursors.DictCursor)

sql = "SELECT ToggleLED FROM students WHERE id=5;"

cur.execute(sql)

ledValue = cur.fetchone()

db.autocommit(True)
if ledValue = True:
	print "LED on"
  GPIO.output(18,GPIO.HIGH)
  time.sleep(1)
 elif ledValue = False:
  print "LED off"
  GPIO.output(18,GPIO.LOW)
else:
  print "invalid value,turning led off anyway"
  GPIO.output(18,GPIO.LOW)
cur.close()

db.close()



