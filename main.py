import requests
import colorama
from colorama import Fore
import time
import os
from discord_webhook import DiscordWebhook



def setup_proxies():
    proxies = []
    with open('proxies.txt', 'r') as file:
        proxies = [line.strip() for line in file.readlines()]

    if not proxies:
        exit()

    return {'http': proxies.pop(0), 'https': proxies[0]}

def main():
    req = 0

    print(f"                                              {Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}] 3s timeout at every request so you don't ratelimit!! ")
    time.sleep(3)

    os.system("clear || cls")

    print(f"""{Fore.MAGENTA}

                                                            ╔═╗╔╗╔╦╔═╗╔═╗╦ ╦╦═╗╦  
                                                            ╚═╗║║║║╠═╝║╣ ║ ║╠╦╝║  
                                                            ╚═╝╝╚╝╩╩  ╚═╝╚═╝╩╚═╩═╝
                                                                    SnusXploit Sniper
                                                                                V1
    """)

    prox = input(f"                                                        {Fore.MAGENTA}[{Fore.RESET}USE PROXIES?{Fore.MAGENTA}] (y/n) > ")
    if prox == 'y':
        proxies = setup_proxies()
    wbook = input(f"                                                        {Fore.MAGENTA}[{Fore.RESET}WEBHOOK{Fore.MAGENTA}] > ")
    tken = input(f"                                                        {Fore.MAGENTA}[{Fore.RESET}TOKEN{Fore.MAGENTA}] > ")
    url = input(f"                                                        {Fore.MAGENTA}[{Fore.RESET}URL TO SNIPE{Fore.MAGENTA}] > ")
    guildid = input(f"                                                        {Fore.MAGENTA}[{Fore.RESET}GUILD ID{Fore.MAGENTA}] > ")
    print("")

    claimed = DiscordWebhook(url=wbook, content=f"**discord.gg/{url} Claimed. @everyone**", username="@SnipeURL | SlavSH")
    banned = DiscordWebhook(url=wbook, content=f"**.gg/{url} Banned :(**", username="@SnipeURL | SlavSH")

    api = "https://canary.discord.com/api/v10/invites/"
    claimapi = f"https://discord.com/api/v9/guilds/{guildid}/vanity-url"
    payload = {
        'code': f"{url}"
    }

    headers = {'Authorization': tken, 'Content-Type': 'application/json'}

    while True:
        req+=1
        s = requests.get(f"{api}{url}", proxies=proxies) if prox == 'y' else requests.get(f"{api}{url}")  
        if s.status_code == 200:
            print(f"                                                        {Fore.MAGENTA}[{Fore.RESET}-{Fore.MAGENTA}] .gg/{url} | Unavailable | Sniping it | R:{req}")
            time.sleep(0.1) if prox == 'y' else time.sleep(3)
        elif s.status_code == 404:
            print(f"                                                        {Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}] .gg/{url} | Available | Sniping! | R:{req}")
            w = requests.patch(claimapi, json=payload, headers=headers, proxies=proxies) if prox == 'y' else requests.patch(claimapi, json=payload, headers=headers)  
            if w.status_code == 200:
                claimed.execute()
                print(f"                                                        {Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}] .gg/{url} | Sniped! | R:{req}")
                time.sleep(15)
                return main()
            else:
                banned.execute()
                print(f"                                                        {Fore.MAGENTA}[{Fore.RESET}:({Fore.MAGENTA}] .gg/{url} | Error! Probably Banned. | Status Code: {w.status_code} | R:{req}")
                time.sleep(15)
                return main()
main()