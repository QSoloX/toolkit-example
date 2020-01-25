# Help Text
from colorama import Fore
import requests


word_list_crawl_options = {"url": ["", "Required"], "list": "url_list.aawt"}
word_list_crawl_help_text = "A web crawler based of off a wordlist."
word_list_crawl_results = []


def word_list_crawl(arguments):
    url, url_list = arguments
    urls_to_scrape = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
    with open("payloads/word_lists/"+url_list, 'r') as f:
        url_array = []
        for line in f:
            url_array.append(line.strip("\n"))
    for i in url_array:
        print(f"{Fore.LIGHTGREEN_EX}trying.... {url}/{i}")
        r = requests.get(f"{url}/{i}",
                         headers=headers)
        if r.status_code == 200:
            print(f"{Fore.MAGENTA}/{i} found!")
            if not '/'+i in word_list_crawl_results:
                word_list_crawl_results.append("/" + i)
                urls_to_scrape.append("/" + i)
