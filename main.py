print("Hello, World!")
import telebot
from telebot import types
from telebot.types import InlineKeyboardButton , InlineKeyboardMarkup

tbT = "5639296247:AAHYQdeXMkM-cHOybxmA2bBriuD6FOy6Vgk"
tb = telebot.TeleBot(tbT)

@tb.message_handler(commands=["start"])
def starting(m):
    devID= 1655098601
    if m.from_user.id == devID :
        tb.reply_to(m, "yo")
##parse_mode=MARKDOWN

#buttons
channelButton = InlineKeyboardButton(
    "↫❨ＳＣ❩↬" , url="https://t.me/QQQQvQvv"
)

owner_accunt = InlineKeyboardButton(
    "↫❨ＯＷＮＥＲ❩↬", url="https://t.me/nnko0o"
)

@tb.message_handler(commands=["bc"])
def bc_cmd(m):
    t = m.text.replace("/bc", "")
    
    markup = InlineKeyboardMarkup()
    
    markup.add( channelButton , owner_accunt )
   
    tb.send_message(m.chat.id ,   text="هايزنبرغ", 
    reply_markup = markup )
    
    tb.reply_to(m,
    "the message is sended\nThe Message is:\n{t}\n..." .format(t=t)
    )

#@tb.message_handler(func= lambda m: True)
#def ssss4(m):
#        tb.send_message(chat_id=m.chat.id,
#        text=m.id
#        )    
#        
#@tb.message_handler(content_types=["voice"])
#def photoHandle(m):
#    a1 = m.voice.file_id
#    tb.reply_to(m, a1)
#    tb.send_voice(m.chat.id, a1)
                                
tb.delete_webhook()
print ("the bot is runnig...")
tb.infinity_polling()
