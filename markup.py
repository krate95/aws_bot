from telebot.types import ReplyKeyboardMarkup, InlineKeyboardButton
from config import *

def get_menu_markup():
    
    markup = ReplyKeyboardMarkup(one_time_keyboard = False)
    for i in MENU:
        markup.row(InlineKeyboardButton(text = i))
        
    return markup
