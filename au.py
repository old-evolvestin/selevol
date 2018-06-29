# -*- coding: utf-8 -*-

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import telebot
from telebot import types
import urllib3
import re
import requests
import time
from time import sleep
import datetime
from datetime import datetime
import _thread
import random

# ======================================================================================================================
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds1 = ServiceAccountCredentials.from_json_keyfile_name('auction1.json', scope)
creds2 = ServiceAccountCredentials.from_json_keyfile_name('auction2.json', scope)
client1 = gspread.authorize(creds1)
client2 = gspread.authorize(creds2)
sheet1 = client1.open('Users-Auction').sheet1
sheet2 = client2.open('Users-Auction').sheet1
itemsheet1 = client1.open('Items-Auction').sheet1
itemsheet2 = client2.open('Items-Auction').sheet1
g_lotnames = itemsheet1.row_values(1)
tkn = '587974580:AAFGcUwspPdr2pU44nJqLD-ps9FxSwUJ6mg'#chats1[0]
bot = telebot.TeleBot(tkn)

less = '🌲'
gori = '⛰'
gold = '💰'

atk = '⚔️'
deff = '🛡'
mo = '🇲🇴'
gp = '🇬🇵'
cy = '🇨🇾'
va = '🇻🇦'
im = '🇮🇲'
eu = '🇪🇺'
ki = '🇰🇮'
skal = '🖤'
bats = '🦇'
turt = '🐢'
oplt = '☘️'
rose = '🌹'
farm = '🍆'
ambr = '🍁'

adress = 1300

idMe = 396978030
idChatDevelopment = -1001186759363

# ======================================================================================================================
bot.send_message(idMe, '🤤')


def rawtime(stamp):
    rtime = []
    weekday = datetime.utcfromtimestamp(int(stamp + 3 * 60 * 60)).strftime('%a')
    if weekday == 'Mon':
        weekday = 'Пн'
    elif weekday == 'Tue':
        weekday = 'Вт'
    elif weekday == 'Wed':
        weekday = 'Ср'
    elif weekday == 'Thu':
        weekday = 'Чт'
    elif weekday == 'Fri':
        weekday = 'Пт'
    elif weekday == 'Sat':
        weekday = 'Сб'
    elif weekday == 'Sun':
        weekday = 'Вс'
    day = datetime.utcfromtimestamp(int(stamp + 3 * 60 * 60)).strftime('%d')
    month = datetime.utcfromtimestamp(int(stamp + 3 * 60 * 60)).strftime('%m')
    year = datetime.utcfromtimestamp(int(stamp + 3 * 60 * 60)).strftime('%Y')
    hours = datetime.utcfromtimestamp(int(stamp + 3 * 60 * 60)).strftime('%H')
    minutes = datetime.utcfromtimestamp(int(stamp)).strftime('%M')
    seconds = datetime.utcfromtimestamp(int(stamp)).strftime('%S')
    rtime.append(weekday)
    rtime.append(day)
    rtime.append(month)
    rtime.append(year)
    rtime.append(hours)
    rtime.append(minutes)
    rtime.append(seconds)
    return rtime


def rawtime_lite(stamp):
    rtime = []
    hours = datetime.utcfromtimestamp(int(stamp + 3 * 60 * 60)).strftime('%H')
    minutes = datetime.utcfromtimestamp(int(stamp)).strftime('%M')
    seconds = datetime.utcfromtimestamp(int(stamp)).strftime('%S')
    rtime.append(hours)
    rtime.append(minutes)
    rtime.append(seconds)
    return rtime


@bot.message_handler(commands=['time'])
def handle_time_command(message):
    time = rawtime(int(datetime.now().timestamp()))
    text = 'Время: ' + str(time[4]) + ':' + str(time[5]) + ':' + str(time[6]) + \
        ' <code>(' + str(time[0]) + ' ' + str(time[1] + '.' + str(time[2]) + '.' + \
        str(time[3])) + ', GMT+3)</code>'
    bot.send_message(message.chat.id, text, parse_mode='HTML')


@bot.message_handler(commands=['id'])
def handle_id_command(message):
    if message.reply_to_message is None:
        text = 'Твой ID: <code>' + str(message.from_user.id) + '</code>\n'
        if message.chat.id < 0:
            text = text + 'Group ID: <code>' + str(message.chat.id) + '</code>'
    elif message.reply_to_message:
        id = str(message.reply_to_message.from_user.id)
        if message.reply_to_message.from_user.username:
            username = '@' + str(message.reply_to_message.from_user.username)
        else:
            username = ''
        if message.reply_to_message.from_user.first_name:
            firstname = str(message.reply_to_message.from_user.first_name)
        else:
            firstname = ''
        if message.reply_to_message.from_user.last_name:
            lastname = str(message.reply_to_message.from_user.last_name)
        else:
            lastname = ''

        signature = str(message.reply_to_message.from_user.is_bot)
        isbot = 'Тип: '
        if signature == 'True' and username == '@rockebolbot':
            isbot = isbot + '<b>Ето я</b>🖤'
        elif signature == 'True':
            isbot = isbot + '<b>Бот</b>'
        elif signature == 'False':
            isbot = isbot + '<b>Человек</b>'
        else:
            isbot = ''

        text = firstname + ' ' + lastname + ' [<b>' + username + '</b>]\n' + \
            'ID: <code>' + id + '</code>\n' + isbot

    bot.send_message(message.chat.id, text, parse_mode='HTML')


@bot.message_handler(commands=['start'])
def handle_start_command(message):
    if message.chat.id > 0:
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        button = []
        button.append(types.InlineKeyboardButton(text='Я шпион🕵🏿', callback_data='Spy'))
        button.append(types.InlineKeyboardButton(text='Нет😡', callback_data='NoSpy'))
        spy = 0
        if spy == 1:
            text = 'Привет шпион\n' \
                   'Зачем жмякаешь /start? Впрочем, не важно. Думаю, ты продолжишь слать мне пины исправно🤤'
            button = []
        else:
            text = 'Привет. Не будем всё усложнять, ладно? Просто скажи, будешь ли ты для нас шпионом?'
        keyboard.add(*button)
        bot.send_message(message.chat.id, text, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
    if call.message.chat.id > 0:
        kek = 0


@bot.message_handler(content_types=["new_chat_members"])
def get_new_member(message):
    if message.chat.title:
        title = str(message.chat.title) + ' ('
    else:
        title = ' ('
    user_id = str(message.from_user.id)
    chat_id = str(message.chat.id)
    if message.from_user.username:
        chat_user = '@' + str(message.from_user.username) + ' / '
    else:
        if message.from_user.first_name:
            firstname = str(message.from_user.first_name)
        else:
            firstname = ''
        if message.from_user.last_name:
            lastname = str(message.from_user.last_name) + ' '
        else:
            lastname = ''
        chat_user = firstname + ' ' + lastname

    if message.new_chat_member is not None and message.new_chat_member.username == 'rockebolbot':
        bot.send_message(idChatDevelopment,
                         chat_user + user_id + ': Добавил бота в чат: ' + title + chat_id + ')')


@bot.message_handler(content_types=['audio', 'video', 'document', 'location', 'contact', 'sticker', 'voice'])
def redmessages(message):
    kek = 0


@bot.message_handler(func=lambda message: message.text)
def repeat_all_messages(message):
    if message.chat.id > 0:
        kek = 0


def detector():
    while True:
        try:
            global itemsheet1
            global adress
            text = requests.get('https://t.me/chatwars3/' + str(adress))
            search = re.search(
                'Лот #(\d+) : (.*)\nПродавец: (.*)\nТекущая цена: (\d+) 👝\nПокупатель: .+\nСрок: .*1060 (.*)',
                str(text.text))
            if search:
                name = search.group(2)
                ench = re.search('(⚡️)', name)
                if ench:
                    name = re.sub('⚡️\+\d+ ', '', name)
                try:
                    google = itemsheet1.row_values(1)
                except:
                    creds1 = ServiceAccountCredentials.from_json_keyfile_name('auction1.json', scope)
                    client1 = gspread.authorize(creds1)
                    itemsheet1 = client1.open('Items-Auction').sheet1
                    google = itemsheet1.row_values(1)
                if name not in google:
                    itemsheet1.update_cell(1, len(google) + 1, name)
                adress = adress + 1
        except Exception as e:
            sleep(0.9)


def telepol():
    try:
        bot.polling(none_stop=True, timeout=60)
    except:
        bot.stop_polling()
        sleep(0.5)
        telepol()


if __name__ == '__main__':
    _thread.start_new_thread(detector, ())
    telepol()