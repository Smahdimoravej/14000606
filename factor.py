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
    chat_id_admin = "202910393"
    if update.effective_message.chat_id == 202910393:
        chat_id_reply = update.message.reply_to_message.forward_from.id
        try:
            bot.forward_message(
                chat_id=chat_id_reply,
                from_chat_id=chat_id_admin,
                message_id=update.message.message_id
            )
            bot.send_message(
                chat_id=update.effective_message.chat_id,
                text="ادمین عزیزفرستادی"
            )

        except Exception as e:
            print("error")
    try:
        bot.forward_message(
            chat_id=chat_id_admin,
            from_chat_id=update.message.chat_id,
            message_id=update.message.message_id
        )
        bot.send_message(
            chat_id=update.message.chat_id,
            # from_chat_id="202910393",
            # from_chat_id=update.effective_message.chat_id,
            text="پیام شما با موفقیت ارسال گردید."
        )
        query_question = "INSERT INTO question (update_id) values ('{}')".format(
            update.message.text)
        query_reply_to_message = "INSERT INTO answers (update_id) values ('{}')".format(
            update.message.reply_to_message.text)
        print(query_question)
        print(query_reply_to_message)
        mycursor.execute(query_question)
        mycursor.execute(query_reply_to_message)
        mydb.commit()
    except Exception as e:
        print("error")


# data = [(Update.update_id)]
# values = ', '.join(map(str, data))
dispatcher.add_handler(MessageHandler(
    Filters.text,
    messagetoUs))

updater.start_polling()