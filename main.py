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
    for character in random.choices("abcdefghijklmnopqrstuvwxyz1234567890", k=2):
        user = user + character
    response = requests.get(f"https://discord.com/api/v9/invites/{user}?with_counts=true&with_expiration=true")
    print(Fore.RESET + Fore.GREEN + f"Available: {user}")
    data =(user)
    discord.post(content=F"**Free Vanity : `{user}` **")
    time.sleep(0.00005)
    
    users = ""
    for characters in random.choices("1234567890qwertyuiopasdfghjklzxcvbnm", k=3):
        users = users + characters
    response = requests.get(f"https://discord.com/api/v9/invites/{users}?with_counts=true&with_expiration=true")
    print(Fore.RESET + Fore.GREEN + f"Available: {users}")
    data =(users)
    discord.post(content=F"**Free Vanity : `{users}` **")
    time.sleep(0.00005)
    

    users = ""
    for characters in random.choices("1234567890qwertyuiopasdfghjklzxcvbnm", k=4):
        users = users + characters
    response = requests.get(f"https://discord.com/api/v9/invites/{users}?with_counts=true&with_expiration=true")
    print(Fore.RESET + Fore.GREEN + f"Available: {users}")
    data =(users)
    discord.post(content=F"**Free Vanity : `{users}` **")
    time.sleep(0.00005)
    