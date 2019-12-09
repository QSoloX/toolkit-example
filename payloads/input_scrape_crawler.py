# Help Text
import requests
from bs4 import BeautifulSoup
from colorama import Fore

# Define options for use in the shell
input_scrape_crawler_options = {"url": ["", "Required"]}
input_scrape_crawler_help_text = "A webcrawler that finds input forms."


# Define custom payload
def input_scrape_crawler(arguments):
    url = arguments
    # Define Variables
    run = True
    results = []
    urls_to_scrape = []
    input_found = []
    input_thing = []

    # Make first request
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    tags = soup.find_all('a')
    input_tags = soup.find_all('form')
    try:
        while run:
            for tag in tags:
                if not tag.get('href') in results and tag.get('href') != "/" and tag.get('href') != "#" and tag.get('href') != "None" and tag.get('href') != None:
                    if input_tags:
                        results.append(tag.get('href'))
                        urls_to_scrape.append(tag.get('href'))
                        print(
                            f"{Fore.GREEN}=> {tag.get('href')} <= found!")
            if urls_to_scrape:
                if input_tags:
                    for form in input_tags:
                        if not form in input_found:
                            input_found.append(form)
                            input_thing.append(
                                url + urls_to_scrape[0])
                            print(
                                f"{Fore.LIGHTBLUE_EX}=> {url + urls_to_scrape[0]} has a input tag <= input tag!")
                if "https" not in urls_to_scrape[0] and "www." not in urls_to_scrape[0] and urls_to_scrape[0] != "":
                    if urls_to_scrape[0][0] != "/":
                        urls_to_scrape[0] = "/" + \
                            urls_to_scrape[0]
                    try:
                        r = requests.get(
                            url + urls_to_scrape[0])
                        soup = BeautifulSoup(r.text, 'html.parser')
                        tags = soup.find_all('a')
                        input_tags = soup.find_all('form')
                    except Exception as e:
                        print(e)

                urls_to_scrape.remove(urls_to_scrape[0])
            else:
                print(urls_to_scrape)
                run = False
    except KeyboardInterrupt:
        run = False
