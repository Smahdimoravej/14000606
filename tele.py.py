from telegram import *
from telegram.ext import *
token = "1895042623:AAFpxW23oTtvIuIF70B6LoqNnW9vwbsT6Kw"
bot = Bot(token)
updater = Updater(token, use_context=True)
dispatcher: Dispatcher = updater.dispatcher
 
keyboard_1 = [
            [InlineKeyboardButton("ارتباط با ما", callback_data="contact_us")],
            [InlineKeyboardButton("درباره ی ما", callback_data="about_us")],
            [InlineKeyboardButton("منو", callback_data="menu")],
            [InlineKeyboardButton("خیریه", callback_data="charity")],
            [InlineKeyboardButton("مشخصات جغرافیایی فروشگاه",
             callback_data="location")],
            [InlineKeyboardButton("سفارشات", callback_data="orders")],
            [InlineKeyboardButton("درباره ی طراح ربات",
             callback_data="about_creator_of_bot")],
            [InlineKeyboardButton("نظرات کاربران",
             callback_data="comments")]
    ]
keyboard_2 = [
            [InlineKeyboardButton("جوجه", callback_data="juje")],
            [InlineKeyboardButton("کباب", callback_data="kabab")],
            [InlineKeyboardButton("خورش قیمه", callback_data="gheime")],
            [InlineKeyboardButton("خورش سبزی", callback_data="sabzi")],
            [InlineKeyboardButton("پلو باقاله", callback_data="polo_baghelle")],
            ]
reply_mark_1 = InlineKeyboardMarkup(keyboard_1)
reply_mark_2 = InlineKeyboardMarkup(keyboard_2)


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
            text="پیام شما با موفقیت ارسال گردید.",
            reply_markup=reply_mark_1
        )
    except Exception as e:
        print("error")


def query_btns(update: Update, context: CallbackContext):
    query: CallbackQuery = update.callback_query
    if query.data == "contact_us":
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text="شماره تماس با مدیریت: ---------"
            )
    elif query.data == "about_us":
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text="رستوران داش علی با 20 سال سابقه آمادهی پذیرایی می باشد."
            )
    elif query.data == "menu":
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text="به به چه غذایی سفارش دادی.دلم خواست",
            reply_markup=reply_mark_2
            )
    elif query.data == "charity":
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text="شما می توانید ما را در اطعام نیاز مندان کمک کنید. شماره کارت:"
            )
    elif query.data == "orders":
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text="،سفارشتات خود را به ما اطلاع دهید.تا ساعت 12شب روز قبل می توانید",
            )
    elif query.data == "about_creator_of_bot":
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text="بذار گمنام بمونم"
        )
    elif query.data == "comments":
        bot.send_message(
            chat_id=update.effective_message.chat_id,
            text="کار داره هنوز"
        )


dispatcher.add_handler(MessageHandler(
    Filters.text, messagetoUs))
dispatcher.add_handler(CallbackQueryHandler(query_btns))
updater.start_polling()
