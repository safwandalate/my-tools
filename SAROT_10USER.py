import random, sys
import time
import requests
import os, pyfiglet
import webbrowser
import sys as n
import time as mm
#--------------------------------------------»
S = "\033[1;91m"  #احمر
B = "\033[1;90m"  #اسود فاتح
C = "\033[1;97m"  #ابيض
E = "\033[1;92m"  #اخضر
H = "\033[1;93m"  #اصفر
K = "\033[1;94m"  #ازرق
L = "\033[1;95m"  #ارجواني
M = "("
M = ")"
#--------------------------------------------»

log = pyfiglet.figlet_format("SAROT")
print(E+log+'\n py : @B_5_U')
print(H+'⌯'*33)
print('\n\n')
ID = input (E+ '        - ID '+S+'› › '+H)
print('\n\n')
token = input(E+  '        - TOKEN'  +S+ '› › '+H)
os.system('clear')
print('py : @B_5_U \n𝚆𝚊𝚒𝚝 ...\n- - - -'+E+'ᑅ ᐧ ᑀ'+H+'- - - -\n')


ss = 1

saarot='QWERTYUIOPLKJHGFDSAZXCVBNM'
ssarot = '0987654321ABCDEFGHIKLMNOPQSTVWSYZ'
sarott = 1
while True:
   s= ''.join(random.sample(ssarot,sarott,))
   a= ''.join(random.sample(saarot,sarott))
   Sar=(a+a+a+s+a+a+a)#1
   sarotyy=(a+a+s+a+a+a+a)
   SarO=(a+a+a+a+s+a+a)
   SaO=(a+a+s+a+a+a)#4
   SoO=(a+a+a+s+a+a)
   SAR=(a+a+a+a+a+s)
   SRO=(a+a+a+a+a+a+s)
   SSRA=(a+a+a+a+a+s+a)
   SaRoTy=(a+a+a+a+a+a)
   sarOT=(a+a+a+a+a+a+a)
   s1arot=(a+a+s+s+a+a)
   syr = Sar , sarotyy , SarO , SaO , SoO , SAR , SAR , SSRA , s1arot , sarOT , SaRoTy ,
   sarot = str("".join(random.choice(syr)))
   url = f"https://t.me/{sarot}"
   req = requests.get(url)
   if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0: 
    print(f'{E}«{ss}»:𝚌𝚑𝚎𝚌𝚔›› {sarot}')
   

    
    try:
     req = requests.post(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌯ 𝚌𝚑𝚎𝚌𝚔
┅ ┅ ┅ ┅ ┅ ┅
@{sarot}
┅ ┅ ┅ ┅ ┅ ┅
⌯ py : @B_5_U''')


     
    except NameError:
     pass
   else:
    print(f'''{S}«{ss}»|𝚋𝚊𝚍›› {sarot}''')
   ss += 1