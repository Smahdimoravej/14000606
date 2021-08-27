from telegram import *
from telegram.ext import *
import mysql.connector
mydb = mysql.connector.connect(
    user="seyed",
    password="Sm13481353",
    host="localhost",
    database="telegram_bot",
    auth_plugin="mysql_native_password"
    )
mycursor = mydb.cursor()
token = "1895042623:AAFpxW23oTtvIuIF70B6LoqNnW9vwbsT6Kw"
bot = Bot(token)
updater = Updater(token, use_context=True)
dispatcher: Dispatcher = updater.dispatcher


def messagetoUs(update: Update, context: CallbackContext):
    print(update)
    if update.message.reply_to_message.chat_id != 0:
    # if update.message.reply_to_message.chat_id is True نشد:
        print("ok")
        try:
            bot.forward_message(
                chat_id="202910393",
                from_chat_id=update.message.reply_to_message.chat_id,
                message_id=update.message.reply_to_message.message_id
            )
            bot.forward_message(
                chat_id="202910393",
                from_chat_id=update.message.chat_id,
                message_id=update.message.message_id
            )
        except Exception as e:
            print("error")
        query_question = "INSERT INTO question (first_message) values ('{}')".format(
            update.message.reply_to_message.text)
        query_reply_to_message = "INSERT INTO answers (reply_message) values ('{}')".format(
            update.message.text)
        print(query_question)
        print(query_reply_to_message)
        mycursor.execute(query_question)
        mycursor.execute(query_reply_to_message)
        mydb.commit()


dispatcher.add_handler(MessageHandler(
    Filters.text,
    messagetoUs))
updater.start_polling()
