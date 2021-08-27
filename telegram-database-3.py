import mysql.connector
# config  =  {
#     "user":"root",
#     "password":"Sm13481353",
#     "host":"3"
# }
mydb = mysql.connector.connect(
    user="seyed",
    password="Sm13481353",
    host="localhost",
    database="telegram_bot",
    auth_plugin="mysql_native_password"
    )
mycursor = mydb.cursor()
query = "select * from question where update_id = 40"
mycursor.execute(query)
result = mycursor.fetchall()
for r in result:
    print(r)
