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

query = "update question set update_id = 60 where id = 1"
mycursor.execute(query)
mydb.commit()
