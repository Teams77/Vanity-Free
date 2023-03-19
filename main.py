import requests, random, time , json##By Team 77 
from colorama import Fore##By Team 77 
from discordwebhook import Discord    ##By Team 77 
##By Team 77 
with open('config.json') as config_file:##By Team 77 
    config = json.load(config_file)##By Team 77 
webhook = config["webhook"]##By Team 77 ##By Team 77 
##By Team 77 
##By Team 77 
discord = Discord(url=webhook) ##Enter Webhook Here
error = 0##By Team 77 
while True:##By Team 77 
    user = ""##By Team 77 
    for character in random.choices("abcdefghijklmnopqrstuvwxyz1234567890", k=2): ##By Team 77 ##By Team 77 
        user = user + character##By Team 77 
    response = requests.get(f"https://discord.com/api/v9/invites/{user}?with_counts=true&with_expiration=true")##By Team 77 
    print(Fore.RESET + Fore.GREEN + f"Available: {user}")##By Team 77 
    data =(user)##By Team 77 
    discord.post(content=F"**Free Vanity : `{user}` **")##By Team 77 
    time.sleep(0.00005)##By Team 77 
    
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
        users = users + characters##By Team 77 
    response = requests.get(f"https://discord.com/api/v9/invites/{users}?with_counts=true&with_expiration=true")##By Team 77 
    print(Fore.RESET + Fore.GREEN + f"Available: {users}")##By Team 77 
    data =(users)##By Team 77 
    discord.post(content=F"**Free Vanity : `{users}` **")##By Team 77 
    time.sleep(0.00005)##By Team 77 
    
