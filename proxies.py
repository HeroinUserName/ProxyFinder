import requests
from bs4 import BeautifulSoup
import random
import time
from colorama import Fore, init  # We use colorama to colorize the text

# Initialize colorama
init(autoreset=True)

# URL for proxy lists
proxy_sources = [
    # Existing popular sources
    "https://www.sslproxies.org/",  # SSLProxies
    "https://www.freeproxylists.net/",  # Free Proxy Lists
    "https://www.us-proxy.org/",  # US Proxy
    "https://www.socks-proxy.net/",  # SOCKS Proxy List
    "https://www.proxy-list.download/",  # Proxy List Download
    "https://www.freeproxylist.com/",  # Free Proxy List
    "https://www.proxy-listen.de/Proxy/Proxyliste.html",  # Proxy Listen
    "https://www.proxynova.com/proxy-server-list/",  # Proxy Nova
    "https://www.spys.one/en/free-proxy-list/",  # Spys.one Proxy
    "https://www.getproxylist.com/",  # Get Proxy List
    "https://www.cool-proxy.net/",  # Cool Proxy
    "https://www.geonode.com/free-proxy-list/",  # Geonode Proxy List
    "https://www.proxylisty.com/",  # Proxy Listy
    "https://www.proxieslist.com/",  # Proxies List
    "https://www.multiproxy.org/",  # MultiProxy List
    "https://www.xroxy.com/proxylist.htm",  # Xroxy Proxy List
    "https://www.freeproxylist.org/",  # Free Proxy List
    "https://www.proxy-archive.com/",  # Proxy Archive
    "https://www.proxyscan.io/",  # Proxy Scan
    "https://www.proxylists.net/",  # Proxy Lists
    "https://www.proxynova.com/proxy-server-list/",  # Proxy Nova List
    "https://www.openproxy.space/",  # Open Proxy Space
    "https://www.freesockslist.net/",  # Free Socks Proxy List
    "https://www.proxydb.net/",  # Proxy DB

    # GitHub Proxy Sources
    "https://github.com/roosterkid/openproxylist/blob/master/README.md",  # OpenProxyList GitHub Repo
    "https://github.com/Alpaca4/Free-Proxy-List/blob/main/README.md",  # Free Proxy List GitHub Repo
    "https://github.com/iamahmadkhan/Proxy-List/blob/main/README.md",  # Proxy List by Ahmad Khan
    "https://github.com/jetkai/proxy-list/blob/master/README.md",  # Jetkai Proxy List
    "https://github.com/Free-Proxy-List/Free-Proxy-List/blob/main/README.md",  # Free Proxy List Repo
    "https://github.com/AdolfData/ProxyList/blob/main/README.md",  # Proxy List by Adolf Data
    "https://github.com/sushant10pro/Proxy-List/blob/main/README.md",  # Sushant Proxy List
    "https://github.com/theuselessdude/proxy-list/blob/master/README.md",  # Proxy list GitHub by UselessDude
    "https://github.com/jamesacampbell/Proxy-Lists/blob/master/README.md",  # Proxy List by James A. Campbell
    "https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/proxy-servers.txt",  # SecLists Proxy Servers
    "https://github.com/n3r4zzurr0/Proxy-List/blob/master/README.md",  # Proxy List by n3r4zzurr0
    "https://github.com/clarketm/proxy-list/blob/master/README.md",  # Proxy list by clarketm
    "https://github.com/mertguvencli/Proxy-List/blob/main/README.md",  # Mert Guvencli Proxy List
    "https://github.com/mmpx12/proxy-list/blob/main/README.md",  # Proxy list GitHub by mmpx12
    "https://github.com/Kensuke-Motohashi/ProxyList/blob/main/README.md",  # Kensuke Motohashi Proxy List
    "https://github.com/premjith/Proxy-List/blob/master/README.md",  # Premjith Proxy List
    "https://github.com/DavidBuchanan314/proxy-list/blob/master/README.md",  # Proxy list by David Buchanan

    # Additional sources
    "https://www.proxyscrape.com/free-proxy-list",  # Proxy Scrape - updated proxy list
    "https://www.proxylisty.com/free-proxy-list",  # Proxy Listy Free Proxy
    "https://www.proxynova.com/proxy-server-list/country-us/",  # Proxy Nova USA
    "https://www.freeproxylists.com/",  # Free Proxy Lists
    "https://www.proxy-list.org/english/index.php",  # Proxy List Organization
    "https://www.getproxylist.com/",  # Get Proxy List
    "https://www.proxydb.net/",  # Proxy DB
    "https://www.proxyelite.net/",  # Proxy Elite
    "https://www.bestproxylist.com/",  # Best Proxy List
    "https://www.freeproxylist.in/",  # Free Proxy List India
    "https://www.proxystorm.com/free-proxy-list",  # Proxy Storm Free List
    "https://www.torproject.org/",  # Tor Project - proxy sharing
    "https://www.freevpn.org/free-proxy-list/",  # FreeVPN proxy list
    "https://www.proxychecker.co/",  # Proxy Checker List
    "https://www.freesockslist.net/",  # Free Socks Proxy List
    "https://www.bestproxyfinder.com/",  # Best Proxy Finder
    "https://www.xroxy.com/",  # Xroxy Proxy List
    "https://www.proxynova.com/proxy-server-list/country-cn/",  # Proxy Nova China
    "https://www.proxysite.com/",  # Proxy Site
    "https://www.socksproxylist24.top/",  # SOCKS Proxy List
    "https://www.sockslist.net/",  # Socks List
    "https://www.proxysurf.org/",  # Proxy Surf List
    "https://www.freesockslist.net/",  # Free Socks Proxy List
    "https://www.freeproxylist.com/",  # Free Proxy List
    "https://www.vpngate.net/en/proxylist/",  # VPNGate Free Proxy List

    # Additional GitHub repositories with proxy lists
    "https://github.com/Proxy-List/Proxy-List",  # Proxy List Repo by Proxy-List
    "https://github.com/volles/ProxyList",  # Proxy List by Volles
    "https://github.com/FreeProxyList/Proxy-List",  # Free Proxy List Repo
    "https://github.com/moxie0/ProxyList",  # Proxy List by Moxie
    "https://github.com/cyberamigos/Proxy-List",  # Cyber Amigos Proxy List
    "https://github.com/Fabian-Search/Proxy-Lists",  # Fabian Search Proxy List
    "https://github.com/Bob8be/Free-Proxy-List",  # Free Proxy List by Bob8be
    "https://github.com/kevinzhow/proxylist",  # Proxy List by Kevin Zhow
    "https://github.com/SwarajK/go-proxy-list",  # Proxy List by SwarajK
    "https://github.com/Ha3mrX/Proxy-List",  # Proxy List by Ha3mrX
    "https://github.com/Maxio2/proxylist",  # Proxy List by Maxio2
    "https://github.com/techz3000/Proxy-List",  # Proxy List by Techz3000
    "https://github.com/Jarbas/proxy-list",  # Proxy List by Jarbas
]


# Function to fetch proxy list from a given URL
def get_proxies(url):
    proxies = []
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Searching for IP addresses and ports (adjustment based on the page)
        for row in soup.find_all('tr'):
            cols = row.find_all('td')
            if len(cols) > 1:
                ip = cols[0].text.strip()
                port = cols[1].text.strip()
                proxies.append(f"{ip}:{port}")
    except Exception as e:
        print(f"{Fore.RED}Failed to fetch proxies from {url}: {str(e)}")
    return proxies


# Function to check the functionality of a proxy
def check_proxy(proxy):
    url = "https://httpbin.org/ip"  # Test page to verify proxy
    proxies = {
        "http": f"http://{proxy}",
        "https": f"https://{proxy}"
    }
    
    try:
        # Try connecting to httpbin.org via proxy
        response = requests.get(url, proxies=proxies, timeout=10)
        
        if response.status_code == 200:
            print(f"{Fore.GREEN}[VALID] {Fore.LIGHTGREEN_EX}{proxy} {Fore.WHITE}is working fine!")
            return True
        else:
            print(f"{Fore.RED}[INVALID] {Fore.LIGHTBLUE_EX}{proxy} {Fore.WHITE}- {Fore.RED}returned HTTP status code: {response.status_code}")
            return False
            
    except requests.exceptions.Timeout:
        print(f"{Fore.RED}[INVALID] {Fore.LIGHTBLUE_EX}{proxy} {Fore.WHITE}- {Fore.RED}Timeout")
        return False
    except requests.exceptions.ConnectionError:
        print(f"{Fore.RED}[INVALID] {Fore.LIGHTBLUE_EX}{proxy} {Fore.WHITE}- {Fore.RED}Connection error")
        return False
    except requests.exceptions.RequestException as e:
        # Handles other exceptions like HTTPS, SSL issues
        print(f"{Fore.RED}[INVALID] {Fore.LIGHTBLUE_EX}{proxy} {Fore.WHITE}- {Fore.RED}Request error: {str(e)}")
        return False


# Main function to gather proxies and check their status
def main():
    all_proxies = []
    for url in proxy_sources:
        print(f"{Fore.YELLOW}Gathering proxies from {Fore.GREEN}{url}")
        proxies = get_proxies(url)
        all_proxies.extend(proxies)

    print(f"\n{len(all_proxies)} all proxies.")
    working_proxies = []
    invalid_proxies = []

    # Checking for working proxies
    for proxy in all_proxies:
        if check_proxy(proxy):
            working_proxies.append(proxy)
        else:
            invalid_proxies.append(proxy)

        # Adding delay between checks to avoid overloading servers
        time.sleep(random.uniform(0.5, 1.0))

    print(f"\nFound {len(working_proxies)} working proxies.")
    print(f"Found {len(invalid_proxies)} invalid proxies.")

    # Saving working proxies to a file
    with open("working_proxies.txt", "w") as file:
        for proxy in working_proxies:
            file.write(f"{proxy}\n")

    # Saving invalid proxies to a file
    with open("invalid_proxies.txt", "w") as file:
        for proxy in invalid_proxies:
            file.write(f"{proxy}\n")

    print(f"{Fore.GREEN}\nWorking proxies have been saved to 'working_proxies.txt'.")
    print(f"{Fore.RED}Invalid proxies have been saved to 'invalid_proxies.txt'.")


if __name__ == "__main__":
    main()
