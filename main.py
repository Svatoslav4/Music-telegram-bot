import telebot
from telebot import types


bot = telebot.TeleBot('7985806779:AAECH7S44hWattalE25ypuSx3Mmbapkn5sQ')


audio_library = {

    "Top Music":[
        "",
        "",
        "",
    ],

    "Українська музика🎺": [
        "CQACAgIAAxkBAAIDhmeEMsVnJ0ZQSWP_bVAAAZJXP3E2OQACU18AAnJnKEgd-YqEg_7H0TYE",
        "CQACAgIAAxkBAAIDk2eENHPCD-j2etEhlqMwMjd6HLsGAAJeXwACcmcoSLbVS4h8fjuzNgQ",

    ],

    "Miyagi🎵": [
        "CQACAgIAAxkBAAIC7GeEJE6e9_9Ks4o-4Naf1TSfgrDYAALxXgACcmcoSHn9lh6XhLTkNgQ",
        "CQACAgIAAxkBAAIC8GeEJY1EDHPaWtfy9S251on7anlJAAL7XgACcmcoSMKpt4K4oiW7NgQ",
        "CQACAgIAAxkBAAIC8meEJZsMLvb1YNPxFeNfXyneup7XAAL8XgACcmcoSCEUkiAaEWFkNgQ",
        "CQACAgIAAxkBAAIDtGeENndPGdBFXBfy2VOw-4omrNa_AAJkXwACcmcoSO5ydN-rG3DcNgQ",
        "CQACAgIAAxkBAAIDs2eENnfvfV-xUu7aeHWDhpyklmF4AAJjXwACcmcoSArMm7ohDefkNgQ",
        "CQACAgIAAxkBAAIDtWeENneafW0szZmb6qr2Z-9o16opAAJlXwACcmcoSC774ZLZJpgMNgQ",
        "CQACAgIAAxkBAAIDtmeENndrn52Pzt-QLmD0dyRp0DAbAAJmXwACcmcoSF2Rh_-Xzuo1NgQ",
        "CQACAgIAAxkBAAIFO2eESL51rCZrDtm6pf9vGKU112mNAAI-YAACcmcoSFN8IUKmhVQiNgQ",
        "CQACAgIAAxkBAAIFOmeESL5iLKzEJ7Hhcg2LS2zvvR-sAAI9YAACcmcoSEi_kpaFUnaUNgQ",
        "CQACAgIAAxkBAAIFPGeESL6BypGSlfUN5UAt9oz4FnXDAAI_YAACcmcoSKM83NRjd0ELNgQ",
        "CQACAgIAAxkBAAIGRWeES0uvxvZLi7Ma5lY4namiHEV_AAIQbwACLfIgSBCUNqAuPk3QNgQ",
        "CQACAgIAAxkBAAIGRmeES0syll1rq9RE6yDuAAEqaDL_lAACEW8AAi3yIEjyI2g-k0UQnTYE",
        "CQACAgIAAxkBAAIGR2eES0ujZ3bVnsxnUB0gCtRVs7gQAAISbwACLfIgSE6Meol-pFihNgQ",
        "CQACAgIAAxkBAAIGSGeES0u3HTrz2eJnh7D4V2BUHGj4AAITbwACLfIgSFIJvRVmKB74NgQ",
        "CQACAgIAAxkBAAIGSWeES0tS4Gm08g0TWcs0UxUjCnrXAAIUbwACLfIgSFBRB_yRrSDkNgQ"
    ],
    "Для Старичків🧓🏼": [
        "CQACAgIAAxkBAAIDB2eEKeCNhbWvPBe3iteDtuWbEWJuAAIOXwACcmcoSMHgU5QZ-iX7NgQ",
        "CQACAgIAAxkBAAIDDGeEKkTcmGRepX8o6NB1MojeFIvYAAISXwACcmcoSEhpyjyXIKdvNgQ",
        "CQACAgIAAxkBAAIDDWeEKkQd97HrTexvua5GaGf8IGk-AAITXwACcmcoSODGkhaf9uT6NgQ",
        "CQACAgIAAxkBAAIDC2eEKkTmpPOeSZpc-CWgDeFZroZzAAIRXwACcmcoSKJ8R33roNyyNgQ",
        "CQACAgIAAxkBAAIDDmeEKkQplhcQgaSADxeb9v3irBuNAAIUXwACcmcoSHefrnPHQnmuNgQ",
        "CQACAgIAAxkBAAIDD2eEKkRzvD4WR7vH7Q7RGeNNZtxQAAIVXwACcmcoSKp_yiTPTqyINgQ",
        "CQACAgIAAxkBAAIDEGeEKkSmYV5hgIE3hHp0b4Da5waxAAIWXwACcmcoSDWBYbmLFI2mNgQ",
        "CQACAgIAAxkBAAIDiGeEM2xGevFLX7sB0GHYxxBj0aTXAAJUXwACcmcoSLf1xnJ0lxHLNgQ"
    ],

    "Macan 𝑩𝑴𝑾":[
        "CQACAgIAAxkBAAIEMWeEPqTYIXVMaHlGj0SubLNUSP9HAALPXwACcmcoSLH1G34rKymHNgQ",
        "CQACAgIAAxkBAAID6meEPAmYoppfDJjUbGAymoAC7OsPAAKfXwACcmcoSO0P8QWgiNtgNgQ",
        "CQACAgIAAxkBAAID62eEPAmQyyINIXYLiLD3dIvS6YfoAAKgXwACcmcoSAImdQROCkqqNgQ",
        "CQACAgIAAxkBAAIEMmeEPqTXmzJnDq9SFq5BmiKlwdDJAALQXwACcmcoSPN3ookeWGzoNgQ",
        "CQACAgIAAxkBAAIEM2eEPqQYGSQwjkJJRVXdyVKYWbzjAALRXwACcmcoSPqvd3DKKajlNgQ"
    ],
    "Travis Scott👨🏿":[
        "CQACAgIAAxkBAAID8meEPO__4PdGmTjB18fepenw3otHAAKrXwACcmcoSJUrCL4ck5jhNgQ",
        "CQACAgIAAxkBAAID82eEPO_4Ht3E5ShJyUG7zBP0uUFsAAKsXwACcmcoSDT1hiwuykvjNgQ",
        "CQACAgIAAxkBAAID9WeEPO_NNILuaURSGF47q7feeVecAAKuXwACcmcoSDnLIrop_mZHNgQ",
        "CQACAgIAAxkBAAID9WeEPO_NNILuaURSGF47q7feeVecAAKuXwACcmcoSDnLIrop_mZHNgQ"
    ],

    "The Weekend🤩":[
        "CQACAgIAAxkBAAIHBWeFLSCiZzUWZk0o42Il3PfJo81RAAKfawACLfIoSDiBxINQzC4ZNgQ",
        "CQACAgIAAxkBAAIHBGeFLSDS3_gYMucEo8_-AhVrrwbLAAKeawACLfIoSOLcv1hHEiCCNgQ",
        "CQACAgIAAxkBAAIHBmeFLSCjWbRmOX_sq9OGekX-BTiJAAKgawACLfIoSMtBKK5CHFn9NgQ",
        "CQACAgIAAxkBAAIHB2eFLSDefat3tO73x1JvC3XrPlO2AAKhawACLfIoSNyLamHHOBkeNgQ",
        "CQACAgIAAxkBAAIHCGeFLSBp6AxSSgQewnIBLBBq4lUWAAKjawACLfIoSExOCIBxrsJ5NgQ",
        "CQACAgIAAxkBAAIHCWeFLSDH6ahHkGsWl-G0AlUo8tFoAAKkawACLfIoSFh7vhvF98CgNgQ",
        "CQACAgIAAxkBAAIHCmeFLSBozDMQAZs-wKespZrHMr3pAAKmawACLfIoSAPnz-MqudksNgQ",
        "CQACAgIAAxkBAAIHC2eFLSBR-W4b5m5ZN4jkOU88vHWFAAKnawACLfIoSMne3M1bWkpSNgQ",
        "CQACAgIAAxkBAAIHDGeFLSDyl5kCmppep0sTEvIMOxjZAAKoawACLfIoSDeGEAfE8fa1NgQ",
    ],

    "Drake🥷":[
        ""
    ]

}


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привіт! Введіть команду /music для вибору музики,дізнатися інформацію про бота /info.")


@bot.message_handler(commands=['music'])
def music_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button0 = types.KeyboardButton("Top Music")
    markup.row(button0)
    button1 = types.KeyboardButton("Українська музика🎺")
    button2 = types.KeyboardButton("Для Старичків🧓🏼")
    markup.row(button1,button2)
    button3 = types.KeyboardButton("Miyagi🎵")
    button4 = types.KeyboardButton("GYM Music🏋🏼‍♂️")
    markup.row(button3, button4)
    button5 = types.KeyboardButton("Macan 𝑩𝑴𝑾")
    button6 = types.KeyboardButton("Travis Scott👨🏿")
    markup.row(button5,button6)
    button7 = types.KeyboardButton("The Weekend🤩")
    button8 = types.KeyboardButton("Drake🥷🏾")
    markup.row(button7,button8)
    button9 = types.KeyboardButton("Російська музика :(")
    markup.row(button9)
    bot.send_message(message.chat.id, "Виберіть категорію музики:", reply_markup=markup)


# Обробник вибору категорії музики
@bot.message_handler(func=lambda message: message.text in audio_library)
def send_music(message):
    chat_id = message.chat.id
    category = message.text

    if not audio_library[category]:
        bot.send_message(chat_id, "На жаль, у цій категорії поки що немає музики.")
        return

    for file_id in audio_library[category]:
        bot.send_audio(chat_id, file_id, caption="Ось твоя музика! 🎵")

# Обробник завантаження аудіофайлу для отримання file_id
@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    file_id = message.audio.file_id
    bot.reply_to(message, f"Ваш file_id: {file_id}")


@bot.message_handler(commands=['info'])
def send_photo(message):
    with open("Gavenda.jpg","rb") as photo:
        bot.send_photo(message.chat.id,photo,
        caption = "Привіт цей бот розроблений для прослуховування музики в месенджера telegram. Бот несе в собі круті сучасні модні треки,як каже Міша Гавенда-(пиво є-є,пельмені є-є). Любіть пиво та пельмені,слухайте музику в нашому боті. Слава Україні🇺🇦!"
                       )

#@bot.message_handler(content_types=['video','text'])
#def send_video(message):
    #if message.text=="/info":
        #video=open()

bot.polling(non_stop=True)

