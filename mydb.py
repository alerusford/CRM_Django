import mysql.connector

dataBase = mysql.connector.connect(
	host='localhost',
	user='root',
	passwd='alerusford', auth_plugin='mysql_native_password')

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE db_crm")

print("All Done!")
