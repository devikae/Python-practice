# pip install python-telegram-bot
# Terminal 에서 실행하고 인스톨,
import datetime
import os

TOKEN = '5366306520:AAFx4OVSB9NiE1YXdoh-YSMlS-5pfSv_Ock'

from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters, CommandHandler

updater = Updater(token=TOKEN, use_context=True)

def fn_echo(update, context):
    user_id = update.effective_chat.id
    user_text = update.message.text
    print(user_text) #로그용
    context.bot.send_message(chat_id=user_id, text='hi')

def fn_diary(update, context):
    user_id = update.effective_chat.id
    user_text = update.message.text
    print(user_text)  # 로그용
    context.bot.send_message(chat_id=user_id, text='일기를 쓰겠습니다.')

    createFolder('dairy')
    # 폴더 만들어주는 함수 호출 매개변수에 파일명

    now = datetime.datetime.now()
    formatterDate = now.strftime("/home/pc52/PycharmProjects/pythonProject1/week1/day2/dairy/%Y%m%d_dairy.txt")
    # 경로안에 오늘 시간으로 파일 생성

    cut_text = user_text.replace('/dairy', '')
    # dairy 제거

    f = open(formatterDate, 'a')
    f.write(cut_text)
    # 작성 후
    f.close()
    # 닫아서 저장

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            # 폴더명으로 들어온 매개변수 directory로 검색해서 해당 폴더가 없다면
            os.makedirs(directory)
            # 매개변수 이름으로 폴더 생성
    except OSError:
        print('Error: Creating directory. ' + directory)

createFolder('/home/pc52/PycharmProjects/pythonProject1/week1/day2')
# 폴더 만드는 경로



# 메세지를 보내면 핸들러 작동 메세지가 오면 함수를 호출 // 기본메세지
echo_handler = MessageHandler(Filters.text &(~Filters.command), fn_echo)
updater.dispatcher.add_handler(echo_handler)

# /dairy <-- 텍스트 있을 시 실행
updater.dispatcher.add_handler(CommandHandler('dairy', fn_diary))

# 등록
updater.start_polling()
updater.idle()