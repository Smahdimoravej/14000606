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
query = "insert into question(update_id,chat_id) values (40,20)"
# mycursor.execute(query)
# mydb.commit()
mycursor.execute("select * from question")
users = mycursor.fetchall()
for user in users:
    print(user)
