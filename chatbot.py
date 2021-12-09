import json
import boto3
import requests
from telebot import TeleBot
from config import SECRET, BUCKET, SESSION, PLACE
import report as r
import tempfile
import os

def get_bot_token():

    session = boto3.session.Session()
    client = session.client(service_name = 'secretsmanager', region_name = "eu-west-1")
    request = client.get_secret_value(SecretId = SECRET)
    TOKEN = json.loads(request['SecretString'])['TOKEN']
    
    return TOKEN

def get_bot_client():
    
    token = get_bot_token()
    return TeleBot(token)

def message_check(event):
    
    message = json.loads(event['body'])['message']
    chat_id = message['chat']['id']
    sender = message['from']['last_name']
    
    text = message['text']

    
    return chat_id, text, sender
