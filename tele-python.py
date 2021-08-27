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
    # chat_id_admin = "202910393"
    # if update.effective_message.chat_id =  = 202910393:
    # chat_id_reply = update.message.reply_to_message.forward_from.id
    # try:
    #     bot.forward_message(
    #     chat_id = chat_id_reply,
    #     from_chat_id = chat_id_admin,
    #     message_id = update.message.message_id
    #     )
    #     bot.send_message(
    #     chat_id = update.message.chat_id,
    #     text = "پیام با موفقیت ارسال شد.ای ادمین عزیز"
    #     )
    # except:
    #     bot.send_message(
    #     chat_id = update.message.chat_id,
    #     text = "ارسال ناموفق"
    #     )
    # keyboard = [
    #     [InlineKeyboardButton("ادمین",callback_data = "admin")],
    #     [InlineKeyboardButton("درباره ما",callback_data = "about")]
    #     ]
    # reply_mark = InlineKeyboardMarkup(keyboard)

    try:
        # bot.forward_message(
        # chat_id = "202910393",
        # from_chat_id = update.effective_message.chat_id,
        # message_id = update.message.message_id
        # )
        print(update)
        bot.send_message(
            chat_id="202910393",
            # from_chat_id=update.effective_message.chat_id,
            text=update.message.reply_to_message.text,
            # reply_markup=reply_mark
        )
        bot.send_message(
            chat_id="202910393",
            # from_chat_id=update.effective_message.chat_id,
            text=update.message.text,
            # reply_markup=reply_mark
        )
    except Exception as e:
        print("error")
    # def query_btns(update:Update,context:CallbackContext):
    #     query:CallbackQuery = update.callback_query
    #     if query.data =  = "admin":
    #         bot.send_message(
    #             chat_id = update.effective_message.chat_id,
    #             text = "ادمین کارش درسته"
    #     )
    # elif query.data =  = "about":
    #     bot.send_message(
    #     chat_id = update.effective_message.chat_id,
    #     text = "در مورد من بدانید در شرکت آبفای قم"
    #     )


variable = "hello"
my_str = "{0}  javad".format(variable)
print(my_str)

dispatcher.add_handler(MessageHandler(
    Filters.text,
    messagetoUs))
# dispatcher.add_handler(CallbackQueryHandler(query_btns))
updater.start_polling()
# y = str(Update.update_id)
sql = ("INSERT INTO useraccess (update_id) VALUES %s")

query = ("Update.update_id")
mycursor.execute(sql, query)
# x = Update.update_id
# x = str(x)
# query = "insert into telegram_bot (update_id) values{0}".format(x)
# print(query)
# mycursor.execute(query)
mydb.commit()
mydb.close()
