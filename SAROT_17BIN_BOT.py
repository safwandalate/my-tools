#PY : @B_5_U
import requests , os , telebot , random 
from time import sleep
os.system('pip install pyTelegramBotAPI==3.7.6')
os.system('pip install telebot')
token = input('\n\n\033[1;93m- TOKEN \033[1;91m› › ')
os.system('clear')
print('\n\033[1;93m ‹‹ Go To Bot ›› ')
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message,f'''⌯ WELCOME

⌯ To get started send /sarot 
	
⌯ PY : @B_5_U ‹‹
⌯ Brother : @O99_5_O ‹‹
	''')
@bot.message_handler(commands=['sarot'])
def send_sarot(message):
    #PY : @B_5_U
    if message.text == '/sarot':
    	bot.reply_to(message,f'⌯ Start check ...')
    	while 1:
    		sarrot = '5678904321'
    		my=("483","376","536")
    		SAR = str("".join(random.choice(my)for i in range(1)))
    		#</> SAROT ⌯
    		SAROT = str("".join(random.choice(sarrot)for i in range(4)))
    		bn = (f'{SAR}{SAROT}')
    		url = f'https://bin-checker.net/api/{bn}'
    		saroty = requests.get(url).json()
    		te = saroty['type']
    		cd = saroty['country']['code']
    		cy = saroty['country']['name']
    		bk = saroty['bank']['name']
    		sleep(3)
    		bot.send_message(message.chat.id,f'''⌯ 𝐍𝐄𝐖 𝐁𝐈𝐍 \n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n⌯ 𝐁𝐈𝐍 : {bn}\n⌯ 𝐂𝐎𝐔𝐍𝐓𝐑𝐘 : {cy}\n⌯ 𝐓𝐘𝐏𝐄 : {te}\n⌯ 𝐂𝐎𝐈𝐍 : {cd}\n⌯ 𝐁𝐀𝐍𝐊 : {bk}\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n⌯ 𝐏𝐘 : ›› @B_5_U ‹''')
    		print('\033[1;92m'+'</>'+bn+' : '+cy)
bot.polling(True)
#Ꮠ PY : @B_5_U