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
# mycursor.execute("create database telegram_bot")
# mycursor.execute("show databases")
# for db in mycursor:
#     print(db)
# query = "create table question(
# id int auto_increment primary key not null,
# update_id int unique  not null,
# chat_id int unique not null
# )"
# mycursor.execute(query)
mycursor.execute("show tables")
for tb in mycursor:
    print(tb)
mycursor.close
