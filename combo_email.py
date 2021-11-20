import random , os , sys , webbrowser , pyfiglet , time

# ┅  ┅  ┅  ┅  ┅  ┅  ┅  ┅
S = "\033[1;91m"  #احمر
Y = "\033[1;34m" #ازرق فاتح
W = "\033[2;31m"  #احمر ثان
C = "\033[1;97m" #ابيض
B = "\033[1;90m"  #اسود فاتح
C = "\033[1;97m"  #ابيض
E = "\033[1;92m"  #اخضر
H = "\033[1;93m"  #اصفر
K = "\033[1;94m"  #ازرق
L = "\033[1;95m"  #ارجواني
M = "("
M = ")"
# ┅  ┅  ┅  ┅  ┅  ┅  ┅  ┅

R = (S+'∞'*45)
LOGO = pyfiglet.figlet_format("   E M A I L  ")
sssarot = f"""{R}
\033[1;93m‹1› \033[1;92mايميل باسم عشوائي\033[1;93m\n‹2› \033[1;92m ايميل باسم محدد
\033[2;33m‹3› \033[1;92mايميل باسم محدد وباسورد محدد
\033[1;93m‹4› \033[1;92mايميل بدون باسورد
\033[1;93m‹5› \033[1;92mTELE:CHANNEL"""
def AHMED(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(1/236)
AHMED(B+LOGO+'        PY : @B_5_U   PY :  @O99_5_O'+'\n'+sssarot+'\n')
print(S+R)

N = 0
l = ' '
num = '1029384756'
m = '.com'
ps = ('1234512345','1122334455','1234554321','12345678','qwertyuio','123456')

mil = ('ahmed','mohamed','Leona','sara','talla','mark','john','slam','harvel','marvel','aaa','ali','opp','lol')

SaroT = input(''+H+'Ꮠ '+S+'اختر '+H+'Ꮠ\n'+E+'›› ')
if SaroT == '':
	webbrowser.open('https://t.me/pythonvip')
	exit()
if SaroT == '5':
	webbrowser.open('https://t.me/pythonvip')
	exit()
print(l)
print(K+' yahoo , hotmail , gmail\n ')
ahmed = input(''+H+'Ꮠ '+S+'اختر الدومين بدون (@)'+H+'Ꮠ\n'+E+'›› ')
print(l)
SArot = int(input(''+H+'Ꮠ '+S+'العدد'+H+'Ꮠ\n'+E+'›› '))

if SaroT == '1':
	while N < SArot:
		Ss = str(''.join((random.choice(num) for i in range(2))))
		email = random.choice(mil)
		pas = random.choice(ps)
		mail = (email+Ss+'@')
		with open('EMAIL1.txt', 'a+') as SaRoT:
			SaRoT.write(mail+ahmed+m+':'+pas+'\n')
			SaRoT.close()
			print(mail+ahmed+m+':'+pas)
			N=N+1
#TELE ⇩ 			
#⌯ 𝐏𝐘 : @B_5_U

#⌯ 𝐏𝐘 : @O99_5_O
if SaroT == '2':
	print(l)
	saroot = input(''+H+'Ꮠ '+S+'الاسم'+H+'Ꮠ\n'+E+'›› ')
	while N < SArot:
		Ss = str(''.join((random.choice(num) for i in range(2))))
		#email = random.choice(mil)
		pas = random.choice(ps)
		mail = (saroot+Ss+'@')
		with open('EMAIL2.txt', 'a+') as SaRoT:
			SaRoT.write(mail+ahmed+m+':'+pas+'\n')
			SaRoT.close()
			print(mail+ahmed+m+':'+pas)
			N=N+1
#TELE ⇩ 			
#⌯ 𝐏𝐘 : @B_5_U

#⌯ 𝐏𝐘 : @O99_5_O
if SaroT == '3':
	print(l)
	name = input(''+H+'Ꮠ '+S+'الاسم'+H+'Ꮠ\n'+E+'›› ')
	print(l)
	passw = input(''+H+'Ꮠ '+S+'الباسورد'+H+'Ꮠ\n'+E+'›› ')
	while N < SArot:
		Ss = str(''.join((random.choice(num) for i in range(2))))
		mail = (name+Ss+'@')
		with open('EMAIL3.txt', 'a+') as SaRoT:
			SaRoT.write(mail+ahmed+m+':'+passw+'\n')
			SaRoT.close()
			print(mail+ahmed+m+':'+passw)
			N=N+1
#TELE ⇩ 			
#⌯ 𝐏𝐘 : @B_5_U

#⌯ 𝐏𝐘 : @O99_5_O
if SaroT == '4':
	while N < SArot:
		Ss = str(''.join((random.choice(num) for i in range(2))))
		email = random.choice(mil)
		mail = (email+Ss+'@')
		with open('EMAIL4.txt', 'a+') as SaRoT:
			SaRoT.write(mail+ahmed+m+'\n')
			SaRoT.close()
			print(mail+ahmed+m)
			N=N+1
#TELE ⇩ 			
#⌯ 𝐏𝐘 : @B_5_U

#⌯ 𝐏𝐘 : @O99_5_O