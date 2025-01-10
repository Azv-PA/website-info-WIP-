import os 
website = input("enter a url: ")
Ping = os.system('ping')
os.system(f'ping {website}')
os.system('cls')
if Ping == True:
    os.system(f'nslookup {website}')
    if {website} == False: 
        print(f" invaid url or website isnt up")
        