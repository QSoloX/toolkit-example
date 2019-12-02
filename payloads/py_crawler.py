from term_colors import bcolors
from bs4 import BeautifulSoup

import requests

# Options used to laod into shell
options = {"url": "Host Url", "check_input": False}

# Used as the payload to launch


class PyCrawler:
    def __init__(self, url):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        self.url = url
        self.results = []
        self.input = []
        self.urls_to_scrap = []
        self.input_found = []

    def attack(self, checkinput=False):
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

                    if self.urls_to_scrap:
                        if input_tags:
                            for form in input_tags:
                                if not form in self.input_found:
                                    self.input_found.append(form)
                                    self.input.append(
                                        self.url + self.urls_to_scrap[0])
                                    print(
                                        f"{bcolors.FAIL}=> {self.url + self.urls_to_scrap[0]} has a input tag <= input tag!{bcolors.ENDC}")
                        if "https" not in self.urls_to_scrap[0] and "www." not in self.urls_to_scrap[0] and self.urls_to_scrap[0] != "":
                            if self.urls_to_scrap[0][0] != "/":
                                self.urls_to_scrap[0] = "/" + \
                                    self.urls_to_scrap[0]
                            try:
                                r = requests.get(
                                    self.url + self.urls_to_scrap[0])
                            except requests.RequestException as e:
                                print(e)
                            try:
                                soup = BeautifulSoup(r.text, 'html.parser')
                                a_tags = soup.find_all('a')
                                input_tags = soup.find_all('form')
                            except Exception as e:
                                print(e)
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
                    if self.urls_to_scrap:
                        if "https" not in self.urls_to_scrap[0] and "www." not in self.urls_to_scrap[0] and self.urls_to_scrap[0] != "":
                            if self.urls_to_scrap[0][0] != "/":
                                self.urls_to_scrap[0] = "/" + \
                                    self.urls_to_scrap[0]
                            try:
                                r = requests.get(
                                    self.url + self.urls_to_scrap[0])
                                soup = BeautifulSoup(r.text, 'html.parser')
                                tags = soup.find_all('a')
                            except Exception as e:
                                print(e)

                        self.urls_to_scrap.remove(self.urls_to_scrap[0])
                    else:
                        print(self.urls_to_scrap)
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


payload_init = PyCrawler
# payload_attack = web_scrap_crawl
