#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 17:09:29 2020

@author: TH
"""
import javsearch
import javscraper
import scraper 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from time import sleep
#url_ = 'https://www.legendadult.net/search?updated-max=2020-01-30T02:40:00%2B08:00&max-results=40&start=0&by-date=false'
#open_link(url_)



def plus_token():
    tk = 'TOKENISHERE'
    return tk
    

def bop(bot, update):
#    url = 'https://4.bp.blogspot.com/-DT3ZM3WS6X0/Wj9Sa6OaPRI/AAAAAAAABqU/rHWimJMvKGw1XTd4Q3UBfoSm7Og3rujYgCLcBGAs/s1600/1.jpg'
    url = 'https://4.bp.blogspot.com/-DOEGhZBSFko/XjPp7qprduI/AAAAAAABTjE/uyP420R-toABjojL1PDW34-GhPim6hItwCLcBGAsYHQ/s1600/Legendadult.blogspot.com%2B-%2B1.webp'
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)



def main():
    token = plus_token()
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('girlsphoto',scraper.present_image))
    dp.add_handler(CommandHandler('bop', bop))
    dp.add_handler(CommandHandler('randomjav', javscraper.javpop))
    dp.add_handler(MessageHandler(Filters.text, javsearch.search))
    
    updater.start_polling()
    updater.idle()
#def echo(bot, update):
##    global update_id
#    # Request updates after the last update_id
#    
##    for update in bot.get_updates(offset=update_id, timeout=10):
##        update_id = update.update_id + 1
#        
#    print (update.message.text)
#    chat_id = update.message.chat_id
#    bot.send_message(chat_id=chat_id,text = update.message.text)
if __name__ == '__main__':
    main()
    
   
