import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'pass123'
)

cursorObject = database.cursor()


cursorObject.execute("CREATE DATABASE brobandcom")

print("All Done!")