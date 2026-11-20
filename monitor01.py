import json
from pathlib import Path

server01 = Path.home()/ "Desktop"/ "servers01.json"
print("Server status checker")
print("*"*30)
print("1. web-server-01")
print("2. db-server-01")
server = input ("Which server do you want to check its status: ")
with open(server01,'r') as f:
    servers=json.load(f)
if server in servers:
    print(f"{server} is currently {servers[server]}")
    status_change =input("Do you want to change its status y/n: ")
    if status_change == "y":
        if servers[server] == "online":
             servers[server] = "offline"
        else :
             servers[server] = "online"
        with open(server01,'w') as f:
            json.dump(servers,f,indent=4)

        print("Glad to have you")
        print("We hope you have a good day")
    elif status_change == "n":
        print("Glad to have you")
        print("We hope you have a good day")

else:
    print("server not found in the database")


 

