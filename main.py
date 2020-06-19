# -*- coding: utf-8 -*-
import telebot
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")

token = config["AUTHENTICATION"]["BOT_TOKEN"]

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


regexp_for_exact_match = "(^|\s)({})(\s|$)"


@bot.message_handler(regexp=regexp_for_exact_match.format(69))
def handler_69(message):
    bot.reply_to(message, "Найс")


@bot.message_handler(regexp=regexp_for_exact_match.format(69))
def handler_300(message):
    bot.reply_to(message, "Число тракториста")


bot.polling()
