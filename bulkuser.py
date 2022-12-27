import instaloader,os
import requests
os.system("pip install instaloader")
R = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
Y = '\033[1;33m'
W = "\033[0m"
os.system("clear")
logo=(f"""{R}_________Bulk-UserName-To-UserId____________________________________
{Y}[+] TeleGram : scapy
{B}[+] Youtube    : scapy
{G}[+] Telegram  : scapy
{R}________________________________________""")
print(logo)

L = instaloader.Instaloader()
user2 =input(R+"Enter UserName List : ")
for ashux in open(user2,'r').read().splitlines():
	username=str(ashux.split('\n')[0])
	profile = str(instaloader.Profile.from_username(L.context,username))
	idd=str(profile.split(')>')[0])
	id=idd.split(' (')[1]
	print(R+"Username : "+username+G+ " Id Is : "+id)
	print(Y+"Made By ==> scapy")
	with open ('userid.txt','a+') as good :
		good.write(id+'\n')
	