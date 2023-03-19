import requests, random, time , json
from colorama import Fore
from discordwebhook import Discord    

with open('config.json') as config_file:
    config = json.load(config_file)
webhook = config["webhook"]


discord = Discord(url=webhook) ##Enter Webhook Here
error = 0
while True:
    user = ""
    for character in random.choices("abcdefghijklmnopqrstuvwxyz1234567890", k=2): ##By Team 77 
        user = user + character
    response = requests.get(f"https://discord.com/api/v9/invites/{user}?with_counts=true&with_expiration=true")##By Team 77 
    print(Fore.RESET + Fore.GREEN + f"Available: {user}")##By Team 77 
    data =(user)##By Team 77 
    discord.post(content=F"**Free Vanity : `{user}` **")##By Team 77 
    time.sleep(0.00005)
    
    users = ""##By Team 77 
    for characters in random.choices("1234567890qwertyuiopasdfghjklzxcvbnm", k=3):##By Team 77 
        users = users + characters##By Team 77 
    response = requests.get(f"https://discord.com/api/v9/invites/{users}?with_counts=true&with_expiration=true")##By Team 77 
    print(Fore.RESET + Fore.GREEN + f"Available: {users}")##By Team 77 
    data =(users)##By Team 77 
    discord.post(content=F"**Free Vanity : `{users}` **")##By Team 77 
    time.sleep(0.00005)##By Team 77 
    ##By Team 77 
##By Team 77 
    users = ""##By Team 77 
    for characters in random.choices("1234567890qwertyuiopasdfghjklzxcvbnm", k=4):##By Team 77 
        users = users + characters
    response = requests.get(f"https://discord.com/api/v9/invites/{users}?with_counts=true&with_expiration=true")##By Team 77 
    print(Fore.RESET + Fore.GREEN + f"Available: {users}")##By Team 77 
    data =(users)##By Team 77 
    discord.post(content=F"**Free Vanity : `{users}` **")##By Team 77 
    time.sleep(0.00005)##By Team 77 
    
