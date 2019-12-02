from colorama import Fore
import requests


def word_list_crawl(self, list):
    results = []
    urls_to_scrape = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
    with open(list, 'r') as f:
        url_array = []
        for line in f:
            url_array.append(line.strip("\n"))
    for i in url_array:
        print(f"{Fore.LIGHTGREEN_EX}trying.... {self.url}/{i}{}")
        r = requests.get(f"{self.url}/{i}",
                         headers=headers)
        if r.status_code == 200:
            print(f"{Fore.MAGENTA}/{i} found!")
            if not '/'+i in results:
                results.append("/" + i)
                urls_to_scrape.append("/" + i)
