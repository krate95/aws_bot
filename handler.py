
import json
import chatbot as c
import markup as m
import server as s
import os

bot = c.get_bot_client()

def lambda_handler(event, context):
    
    print(json.loads(event['body']))
    chat_id, text, sender = c.message_check(event)
    
    # if sender != 'Dutcosky':
    #     bot.send_message(1192910552, '{} | {}'.format(sender,text))
        
    if text == '/menu':
        bot.send_message(chat_id, "Opciones", reply_markup = m.get_menu_markup())
        
    elif text == '/start':
        bot.send_message(chat_id, "Bot iniciado")
        bot.send_message(chat_id, "Ayuda: /menu")
        
    elif text == '/iniciar':
        bot.send_message(chat_id, "Iniciando server...")
        s.startEC2()
    
    elif text == '/parar':
        bot.send_message(chat_id, "Parando server...")
        s.stopEC2()

    else:
        bot.send_message(chat_id, "No entendí esa wea")
