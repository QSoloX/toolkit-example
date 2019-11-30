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
        self.input = []
        self.urls_to_scrap = []

    def web_scrap_crawl(self, checkinput=False):
        # results = []
        # urls_to_scrap = self.results
        run = True
        r = requests.get(self.url)
        if checkinput:
            soup = BeautifulSoup(r.text, 'html.parser')
            a_tags = soup.find_all('a')
            input_tags = soup.find_all('form')
            try:
                while run:
                    for tag in a_tags:
                        if tag.get('href'):
                            # print(tag.get('href'))
                            if not tag.get('href') in self.results and tag.get('href') != "/" and tag.get('href') != "#" and tag.get('href') != "none" and tag.get('href') != None:
                                if input_tags:
                                    self.results.append(
                                        tag.get('href'))
                                    self.urls_to_scrap.append(tag.get('href'))
                                    print(
                                        f"{bcolors.OKGREEN}=> {tag.get('href')} <= found!{bcolors.ENDC}")
                            # else:
                            #     self.results.append(
                            #         tag.get('href'))
                            #     self.urls_to_scrap.append(tag.get('href'))
                            #     print(
                            #         f"{bcolors.OKGREEN}=> {tag.get('href')} <= found!{bcolors.ENDC}")
                    if input_tags:
                        self.input.append(self.url+self.urls_to_scrap[0])
                        print(
                            f"{bcolors.FAIL}=> {self.url} has a input tag <= input tag!{bcolors.ENDC}")
                    if self.urls_to_scrap:
                        if "https" not in self.urls_to_scrap[0] and "www." not in self.urls_to_scrap[0]:
                            print(self.url + self.urls_to_scrap[0])
                            r = requests.get(self.url + self.urls_to_scrap[0])

                            soup = BeautifulSoup(r.text, 'html.parser')
                            a_tags = soup.find_all('a')
                            input_tags = soup.find_all('form')
                        self.urls_to_scrap.remove(self.urls_to_scrap[0])
                    else:
                        run = False
            except KeyboardInterrupt:
                run = False
        else:
            soup = BeautifulSoup(r.text, 'html.parser')
            tags = soup.find_all('a')
            try:
                while run:
                    for tag in tags:
                        if not tag.get('href') in self.results and tag.get('href') != "/" and tag.get('href') != "#" and tag.get('href') != "None" and tag.get('href') != None:
                            self.results.append(tag.get('href'))
                            self.urls_to_scrap.append(tag.get('href'))

                            print(
                                f"{bcolors.OKGREEN}=> {tag.get('href')} <= found!{bcolors.ENDC}")
                    print(self.url + self.urls_to_scrap[0])
                    if self.urls_to_scrap:
                        if "https" not in self.urls_to_scrap[0] and "www." not in self.urls_to_scrap[0]:
                            r = requests.get(self.url + self.urls_to_scrap[0])
                            print(r.status_code)
                            soup = BeautifulSoup(r.text, 'html.parser')
                            tags = soup.find_all('a')
                        self.urls_to_scrap.remove(self.urls_to_scrap[0])
                    else:
                        run = False
            except KeyboardInterrupt:
                run = False

        # Shows if the list has any duplicates
        # print(f"{bcolors.OKGREEN}{len(set(self.results))} found!{bcolors.ENDC}")
        # print(f"{bcolors.OKGREEN}{len(self.results)} found!{bcolors.ENDC}")

    def word_list_crawl(self, list):
        with open(list, 'r') as f:
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
