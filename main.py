import telebot
import re
import time
import configparser

config = configparser.ConfigParser()
config.read('config.cfg')
bot = telebot.TeleBot(str(config['TELEGRAM_CONFIG']['TOKEN']), parse_mode=None)

def alert_if_error(log_file):
    chat_id = int(config['TELEGRAM_CONFIG']['CHAT_ID'])
    error_text = str(config['ENV_CONFIG']['MSG_ERROR'])
    try:
        with open(log_file, 'r+') as f:
            f.seek(0,2)
            while True:
                line = f.readline()
                pattern_error = 'error|ERROR|Error'
                if not line:
                    time.sleep(0.05)
                    f.flush()
                    continue
                elif re.findall(pattern_error, line):
                    bot.send_message(chat_id, error_text)
    except Exception:
        bot.send_message(chat_id, "Script error: " + str(Exception) )

alert_if_error(str(config['ENV_CONFIG']['LOG_FILEPATH']))
bot.infinity_polling()















