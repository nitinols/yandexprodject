import sys
import telebot
import sqlite3
import json

bot = telebot.TeleBot(str(sys.argv[1]))


def main_init(login_info, table_name, bd_name='/main.bd'):
    global bot
    conn = sqlite3.connect(bd_name)
    cursor = conn.cursor()
    a = cursor.execute(f"""SELECT setting FROM {table_name} WHERE login_info == {login_info} """).fetchall()


@bot.message_handler(commands=['start'])
def start_message(message):
    pass


@bot.message_handler(content_types=['text'])
def need_info(message):

    pass


def func_controller(json_file):
    global function_queue, data
    data = json.load(json_file)
    function_queue = data.keys()


def new_func():
    global counter


if __name__ == '__main__':
    main_init(sys.argv[2], sys.argv[3])
    counter = 0
