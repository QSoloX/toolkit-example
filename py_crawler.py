from term_colors import bcolors
from bs4 import BeautifulSoup
import requests


# print results in a grid results

class PyCrawler:
    def __init__(self, url):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        self.url = url
        self.results = []
        self.urls_to_scrap = []

    def web_scrap_crawl(self):
        # results = []
        # urls_to_scrap = self.results
        run = True
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'html.parser')
        tags = soup.find_all('a')
        while run:
            for tag in tags:
                if not tag.get('href') in self.results and tag.get('href') != "/" and tag.get('href') != "#" and tag.get('href') != "none" and tag.get('href') != None:
                    self.results.append(tag.get('href'))
                    self.urls_to_scrap.append(tag.get('href'))

                    print(
                        f"{bcolors.OKGREEN}=> {tag.get('href')} <= found!{bcolors.ENDC}")
            if self.urls_to_scrap and "https" not in self.urls_to_scrap[0] and "www." not in self.urls_to_scrap[0]:
                r = requests.get(self.url + str(self.urls_to_scrap[0]))
                self.urls_to_scrap.remove(self.urls_to_scrap[0])
                soup = BeautifulSoup(r.text, 'html.parser')
                tags = soup.find_all('a')
            else:
                run = False

        # Shows if the list has any duplicates
        # print(f"{bcolors.OKGREEN}{len(set(self.results))} found!{bcolors.ENDC}")
        # print(f"{bcolors.OKGREEN}{len(self.results)} found!{bcolors.ENDC}")

    def word_list_crawl(self):
        with open('url_list.aawt', 'r') as f:
            url_array = []
            for line in f:
                url_array.append(line.strip("\n"))
        for i in url_array:
            print(f"{bcolors.OKBLUE}trying.... {self.url}/{i}{bcolors.ENDC}")
            r = requests.get(f"{self.url}/{i}",
                             headers=self.headers)
            if r.status_code == 200:
                print(f"{bcolors.OKGREEN}/{i} found!{bcolors.ENDC}")
                if not '/'+i in self.results:
                    self.results.append("/" + i)
                    self.urls_to_scrap.append("/" + i)
