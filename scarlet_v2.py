import asyncio
import aiohttp
from aiohttp import ClientSession
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
import time

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def banner():
    print("\033[1;31m")
    print("""
    	███████╗ ██████╗ █████╗ ██████╗ ██╗     ███████╗████████╗
    	██╔════╝██╔════╝██╔══██╗██╔══██╗██║     ██╔════╝╚══██╔══╝
    	███████╗██║     ███████║██████╔╝██║     █████╗     ██║   
    	╚════██║██║     ██╔══██║██╔══██╗██║     ██╔══╝     ██║   
    	███████║╚██████╗██║  ██║██║  ██║███████╗███████╗   ██║   
    	╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝   
                                                         	
                	\033[0;32mCreate by: bot-collab\033[0m

""")

    # Simulando una barra de progreso
    bar_length = 70
    for i in range(bar_length + 1):
        time.sleep(0.05)  # Simular un proceso que toma tiempo
        progress = i * 100 // bar_length
        bar = f"\033[0;34m{'=' * i}\033[0m{' ' * (bar_length - i)}"
        print(f"\r[{bar}] {progress}%", end='', flush=True)
    print("\n\033[0;37m") 

 
 
                                                                                             
                                                                      
async def fetch(url, session):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            content_type = response.headers.get('Content-Type', '').lower()
            if 'text/html' in content_type:
                return await response.text()
            else:
                await response.read()  
                return ''
    except aiohttp.ClientResponseError as e:
        if e.status == 404:
            print(f"{RED}X - Error 404: No encontrada - URL: {url}{RESET}")
        else:
            print(f"{RED}X - HTTP Error: {e.status} - URL: {url}{RESET}")
        return None
    except Exception as e:
        print(f"{RED}X - Error fetching URL: {url} - {e}{RESET}")
        return None

def is_same_domain(base_url, target_url):
    parsed_base_url = urlparse(base_url)
    parsed_target_url = urlparse(target_url)
    base_domain = '.'.join(parsed_base_url.netloc.split('.')[-2:])
    target_domain = '.'.join(parsed_target_url.netloc.split('.')[-2:])
    return base_domain == target_domain

def print_url(url, is_valid, is_subdomain):
    if is_valid:
        status = f"{GREEN}✔{RESET}"
    else:
        status = f"{RED}X{RESET}"

    if is_subdomain:
        color = BLUE
    else:
        color = YELLOW

    print(f"{color}{url}{RESET} - {status}")

async def extract_urls(base_url, url, urls_found, session, queue):
    html = await fetch(url, session)
    if html is not None:
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link.get('href')
            if href:
                full_url = urljoin(base_url, href.strip())
                if is_same_domain(base_url, full_url) and full_url not in urls_found:
                    urls_found.add(full_url)
                    is_subdomain = urlparse(full_url).netloc != urlparse(base_url).netloc
                    print_url(full_url, is_valid=True, is_subdomain=is_subdomain)
                    queue.append(full_url)
    else:
        is_subdomain = urlparse(url).netloc != urlparse(base_url).netloc
        print_url(url, is_valid=False, is_subdomain=is_subdomain)

async def worker(base_url, urls_found, session, queue):
    while queue:
        url = queue.popleft()
        await extract_urls(base_url, url, urls_found, session, queue)

async def main():
    while True:
                base_url = input(str('\033[92mIngrese la url: ')) #'https://www.cajamaynas.pe/'
                print()
                if base_url == '':
                    print("\033[91m[!] Error ingrese una url [!]\033[0;37m")
                    print()
                    base_url = input(str('\033[92mIngrese la url: '))
                    print()
                else:
                    break
                    return
    urls_found = set()
    queue = deque([base_url])

    async with ClientSession() as session:
        workers = [worker(base_url, urls_found, session, queue) for _ in range(10)]
        await asyncio.gather(*workers)

if __name__ == "__main__":
    banner()
    asyncio.run(main())
