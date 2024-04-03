import telebot
import re
import time
import configparser

config = configparser.ConfigParser()
config.read('config.cfg')
bot = telebot.TeleBot(str(config['TELEGRAM_CONFIG']['TOKEN']), parse_mode=None)
bot.infinity_polling()

def alert_if_error(syslog_file):
    with open(syslog_file, 'r+') as f:
        f.seek(0,2)
        while True:
            line = f.readline()
            pattern_name = '\\[[a-z]+\\]'
            pattern_error = 'error|ERROR|Error'
            if not line:
                time.sleep(0.1)
                continue
            elif re.match(pattern_name, line) and re.match(pattern_error, line):
                bot.send_message(int(config['TELEGRAM_CONFIG']['CHAT_ID']), config['TELEGRAM_CONFIG']['MSG_ERROR'])


alert_if_error('/var/log/syslog')















