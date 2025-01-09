import telebot
from telebot import types

bot = telebot.TeleBot('7985806779:AAECH7S44hWattalE25ypuSx3Mmbapkn5sQ')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привіт! Введіть команду /music для вибору музики.")

@bot.message_handler(commands=['music'])
def music_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button0 = types.KeyboardButton("Всі треки в боті")
    markup.row(button0)
    button1 = types.KeyboardButton("Український поп🎺")
    button2 = types.KeyboardButton("Український реп🎤")
    markup.row(button1, button2)
    button3 = types.KeyboardButton("Miyagi🎵")
    button4 = types.KeyboardButton("Для старічків")
    markup.row(button3,button4)
    bot.send_message(message.chat.id, "Привіт! Виберіть категорію музики:", reply_markup=markup)
    bot.register_next_step_handler(message, onclick)

def onclick(message):
    chat_id = message.chat.id

    if message.text == "Український поп🎺":
        audio_files = [
            r"D:/music/artem-pivovarov-klavdia-petrivna-baraban.mp3",
            r"D:/music/dorofeeva-lebiga-a-ya-vse-plakala.mp3",
            r"D:/music/chico-qatoshi-100licya-pokohay-mene.mp3",
            r"D:/music/alyona-alyona-jerry-heil-teresa-maria.mp3"
        ]

    elif message.text == "Український реп🎤":
        audio_files = [
            r"D:/music/yaktak-sobol-poglyad.mp3",
            r"D:/music/.mp3",
            r"D:/music/.mp3"
        ]

    elif message.text == "Miyagi🎵":
        audio_files = [
            r"D:/music/MiyaGi & Andy Panda - Kosandra.mp3",
            r"D:/music/MiyaGi feat. Andy Panda - Utopia.mp3",
            r"D:/music/miyagi-jendshpil-feat.-amigo-samaja.mp3"
        ]

    elif message.text == "Всі треки в боті":
        audio_files = [
            r"D:/music/artem-pivovarov-klavdia-petrivna-baraban.mp3",
            r"D:/music/dorofeeva-lebiga-a-ya-vse-plakala.mp3",
            r"D:/music/chico-qatoshi-100licya-pokohay-mene.mp3",
            r"D:/music/alyona-alyona-jerry-heil-teresa-maria.mp3"
            r"D:/music/MiyaGi & Andy Panda - Kosandra.mp3",
            r"D:/music/MiyaGi feat. Andy Panda - Utopia.mp3",
            r"D:/music/miyagi-jendshpil-feat.-amigo-samaja.mp3",
            r"D:/music/yaktak-sobol-poglyad.mp3"
        ]

    else:
        bot.send_message(chat_id, "Невідома категорія. Спробуйте ще раз.")
        return

    # Надсилаємо файли один за одним
    try:
        for audio_path in audio_files:
            with open(audio_path, 'rb') as audio:
                bot.send_audio(chat_id, audio, caption="Ось твоя музика! 🎵")
    except FileNotFoundError:
        bot.reply_to(message, "Файл не знайдено. Перевір шлях до файлу.")

bot.polling(non_stop=True)
