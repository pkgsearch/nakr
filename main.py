import requests
import random
import time
import os
from colorama import init, Fore

init(autoreset=True)

def banner():
    print(Fore.CYAN + """
█▄░█ ▄▀█ █▄▀ █▀█ █░█ ▀█▀ █▄▀ ▄▀█
█░▀█ █▀█ █░█ █▀▄ █▄█ ░█░ █░█ █▀█
          made by pkgsearch (v2)
    """)

def load_proxies():
    if not os.path.exists("proxies.txt") or os.path.getsize("proxies.txt") == 0:
        print(Fore.YELLOW + "Скачиваю свежие прокси...")
        try:
            r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http", timeout=10)
            with open("proxies.txt", "w") as f:
                f.write(r.text)
            print(Fore.GREEN + f"Загружено {len(r.text.splitlines())} проксей")
        except:
            print(Fore.RED + "Не удалось скачать прокси")
            return []

    with open("proxies.txt", "r") as f:
        proxies = [line.strip() for line in f if line.strip()]
    return proxies

def nakrutka():
    banner()
    url = input(Fore.WHITE + "Введите ссылку на сообщение: ").strip()
    
    if not url.startswith("https://t.me/"):
        print(Fore.RED + "Это не ссылка на ТГ!")
        return

    proxies_list = load_proxies()
    if not proxies_list:
        print(Fore.RED + "Проксей нет :(")
        return

    print(Fore.GREEN + f"Запущена накрутка на {url}")
    print(Fore.YELLOW + "Нажми Ctrl+C чтобы остановить\n")

    try:
        while True:
            proxy = random.choice(proxies_list)
            proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
            
            try:
                requests.get(url, proxies=proxies, timeout=8)
                print(Fore.GREEN + f"[+] Просмотр отправлен | {proxy}")
            except:
                print(Fore.RED + f"[-] Прокси сдох | {proxy}")
            
            time.sleep(1.5)  # ← очень важно!
    except KeyboardInterrupt:
        print(Fore.CYAN + "\nНакрутка остановлена. Пока!")

def main():
    while True:
        banner()
        print(Fore.WHITE + "1 → Обновить прокси")
        print(Fore.WHITE + "2 → Запустить накрутку")
        print(Fore.WHITE + "0 → Выход\n")
        
        choose = input(Fore.WHITE + "Выбор: ")
        
        if choose == "1":
            load_proxies()
        elif choose == "2":
            nakrutka()
        elif choose == "0":
            print(Fore.MAGENTA + "Пока, легенда!")
            break
        else:
            print(Fore.RED + "Неверный выбор!")

if __name__ == "__main__":
    main()
