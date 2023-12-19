import telebot
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton
bot = telebot.TeleBot('6943827016:AAEhybBROEq_iTc2D8cSBqYG3biJ4P_7ZNw')
import pandas as pd
import time
import os

def menu_principal(chat_id):
    markup = InlineKeyboardMarkup(row_width=1)
    botao2 = InlineKeyboardButton('𝐴𝑠𝑠𝑖𝑛𝑎𝑟 𝑜 𝐺𝑟𝑢𝑝𝑜 𝑉𝐼𝑃 🔥', callback_data='botao2')
    botao5 = InlineKeyboardButton('𝐺𝑟𝑢𝑝𝑜 𝐹𝑟𝑒𝑒 👀', url='https://t.me/freevivimendes')
    botao3 = InlineKeyboardButton('𝑃𝑎𝑐𝑘𝑠 𝐸𝑥𝑐𝑙𝑢𝑠𝑖𝑣𝑜𝑠 💎', callback_data='botao3')
    markup.add(botao2,botao5,botao3)
    return markup
#aisjdasidjiasd FUNCIUONA PORRA AIJEDHAIEHUAHE
@bot.message_handler(commands=['start'])
def start(message):
    markup = menu_principal(message.chat.id)

    msg = bot.send_message(message.chat.id, '*𝑉𝑒𝑚 𝑔𝑜𝑧𝑎𝑟 𝑝𝑟𝑎 𝑒𝑠𝑠𝑎 𝑷𝒖𝒕𝒊𝒏𝒉𝒂 🍭👧🏻😈🔥*', parse_mode="MarkdownV2")
    bot.send_photo(message.chat.id, photo='https://i.ibb.co/vXq4RpM/caralho.jpg')
    
    bot.send_message(message.chat.id, text='*      𝑃𝑟𝑜𝑚𝑜çã𝑜 𝑞𝑢𝑎𝑠𝑒 𝑒𝑛𝑐𝑒𝑟𝑟𝑎𝑛𝑑𝑜 🔥❤️‍🔥      *', reply_markup=markup, parse_mode="MarkdownV2")

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'botao2':
        botao2(call.message)
    elif call.data == 'metodopagamento':
        metodopagamento(call.message)
    elif call.data == 'ummes':
        ummes(call.message)
    elif call.data == 'tresmeses':
        tresmeses(call.message)
    elif  call.data == 'seismeses':
        seismeses(call.message)
    elif call.data == 'botao5':
         botao5(call.message)
    elif call.data == 'botao3':
         botao3(call.message)
    elif call.data == 'voltar':
        markup = menu_principal(call.message.chat.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*𝑃𝑟𝑜𝑚𝑜çã𝑜 𝑞𝑢𝑎𝑠𝑒 𝑒𝑛𝑐𝑒𝑟𝑟𝑎𝑛𝑑𝑜 🔥❤️‍🔥*', reply_markup=markup, parse_mode="MarkdownV2")

def botao5(message):
    markup = InlineKeyboardMarkup()
    textozao = '_Então você quer um presentinho 🎁, não é? Para conseguir é muito fácil, é só seguir meus perfis no Instagram e Twitter e mandar print pro meu WhatsApp Estou esperando😈🔥_'
    ig = InlineKeyboardButton('Instagram 📷', url='https://instagram.com/vivimendesshot')
    tt = InlineKeyboardButton('Twitter 🐦', url='https://twitter.com/ViviMen875421')
    wpp = InlineKeyboardButton('WhatsApp 📞', url='https://contate.me/vivimendes')
    voltar = InlineKeyboardButton('𝑉𝑜𝑙𝑡𝑎𝑟 ↩️', callback_data='voltar')
    markup.add(tt, ig, wpp, voltar)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=textozao, reply_markup=markup, parse_mode="MarkdownV2")

def botao2(message):
    markup = InlineKeyboardMarkup()
    texto = '_Qual das minhas ofertas você quer? Efetue o pagamento e receba o acesso IMEDIATO ao grupo de Assinantes\! 💎_'
    mensal = InlineKeyboardButton('1 𝑀ê𝑠',callback_data='ummes')
    #trimestral = InlineKeyboardButton('3 meses R$37,90 ', callback_data='tresmeses')
    vitalicio = InlineKeyboardButton('3 𝑀e𝑠𝑒𝑠', callback_data='seismeses')
    voltar = InlineKeyboardButton('𝑉𝑜𝑙𝑡𝑎𝑟 ↩️', callback_data='voltar')
    markup.add(mensal)
   #markup.add(trimestral)
    markup.add(vitalicio)
    markup.add(voltar)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=texto, reply_markup=markup, parse_mode="MarkdownV2")



def metodopagamento(message):
    markup = InlineKeyboardMarkup()
    escolhe_pagamento = '_Qual vai ser o método de pagamento? 😈_'
    pix = InlineKeyboardButton('𝑃𝑖𝑥 💠', url='google.com')
    cartao = InlineKeyboardButton('𝑪𝒂𝒓𝒕ã𝒐 💳',url='firepoggers.net')
    voltar = InlineKeyboardButton('𝑉𝑜𝑙𝑡𝑎𝑟 ↩️', callback_data='voltar')
    markup.add(pix)
    markup.add(cartao)
    markup.add(voltar)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=escolhe_pagamento, reply_markup=markup, parse_mode="MarkdownV2")


def ummes(message):
    markup = InlineKeyboardMarkup()
    escolhe_pagamento = '_Qual vai ser o método de pagamento? 😈_'
    pix = InlineKeyboardButton('𝑃𝑖𝑥 💠', url='https://botgram.club/vipdaveronica')
    cartao = InlineKeyboardButton('𝑪𝒂𝒓𝒕ã𝒐 💳',url='https://botgram.club/vipdaveronica')
    voltar = InlineKeyboardButton('𝑉𝑜𝑙𝑡𝑎𝑟 ↩️', callback_data='voltar')
    markup.add(pix)
    markup.add(cartao)
    markup.add(voltar)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=escolhe_pagamento, reply_markup=markup, parse_mode="MarkdownV2")

def tresmeses(message):
    markup = InlineKeyboardMarkup()
    escolhe_pagamento = '_Qual vai ser o método de pagamento? 😈_'
    pix = InlineKeyboardButton('𝑃𝑖𝑥 💠', url='https://botgram.club/vip-da-veronica-2')
    cartao = InlineKeyboardButton('𝑪𝒂𝒓𝒕ã𝒐 💳',url='https://botgram.club/vip-da-veronica-2')
    voltar = InlineKeyboardButton('𝑉𝑜𝑙𝑡𝑎𝑟 ↩️', callback_data='voltar')
    markup.add(pix)
    markup.add(cartao)
    markup.add(voltar)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=escolhe_pagamento, reply_markup=markup, parse_mode="MarkdownV2")

def seismeses(message):
    markup = InlineKeyboardMarkup()
    escolhe_pagamento = '_Qual vai ser o método de pagamento? 😈_'
    pix = InlineKeyboardButton('𝑃𝑖𝑥 💠', url='https://botgram.club/vipdaveronica')
    cartao = InlineKeyboardButton('𝑪𝒂𝒓𝒕ã𝒐 💳',url='https://botgram.club/vipdaveronica')
    voltar = InlineKeyboardButton('𝑉𝑜𝑙𝑡𝑎𝑟 ↩️', callback_data='voltar')
    markup.add(pix)
    markup.add(cartao)
    markup.add(voltar)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=escolhe_pagamento, reply_markup=markup, parse_mode="MarkdownV2")


def botao3(message):
    markup = InlineKeyboardMarkup()
    pack1 = 'Pack Bronze de 10 mídias e 5 vídeos R$17,90'
    pack2 = 'Pack prata 20 fotos e 10 vídeos R$35,90'
    pack3 = 'Pack Ouro 40 fotos e 20 vídeos R$79,90'
    faq = '_Meus packs exclusivos estão incluindo fotos e vídeos que NÃO vão para o canal de assinantes, meus conteúdos mais GOSTOSOS e PICANTES 🌶️🔥_'
    bronze = InlineKeyboardButton('𝑻𝒆𝒏𝒉𝒐 𝒊𝒏𝒕𝒆𝒓𝒆𝒔𝒔𝒆 🔥', url='contate.me/vivimendes')
    prata = InlineKeyboardButton('Prata', url='kasjdoasd.com')
    ouro = InlineKeyboardButton('Ouro', url='kasjdoasd.com')
    voltar = InlineKeyboardButton('𝑉𝑜𝑙𝑡𝑎𝑟 ↩️', callback_data='voltar')
    markup.add(bronze)
    markup.add(voltar)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=faq, reply_markup=markup ,parse_mode="MarkdownV2")

# Inicie o bot
bot.infinity_polling()
