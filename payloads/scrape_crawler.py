# Help Text
import requests
from bs4 import BeautifulSoup
from colorama import Fore

# Define options for use in the shell
scrape_crawler_options = {"url": ["", "Required"]}
scrape_crawler_help_text = "A simple web crawler based payload."
scrape_crawler_results = []


# Define custom payload


def scrape_crawler(arguments):
    url = arguments
    # Define Variables
    run = True

    urls_to_scrape = []
    # Make first request
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    tags = soup.find_all('a')
    try:
        while run:
            for tag in tags:
                if not tag.get('href') in scrape_crawler_results and tag.get('href') != "/" and tag.get('href') != "#" and tag.get('href') != "None" and tag.get('href') != None:
                    scrape_crawler_results.append(tag.get('href'))
                    urls_to_scrape.append(tag.get('href'))
                    print(
                        f"{Fore.GREEN}=> {tag.get('href')} <= found!")
            if urls_to_scrape:
                if "https" not in urls_to_scrape[0] and "www." not in urls_to_scrape[0] and urls_to_scrape[0] != "":
                    if urls_to_scrape[0][0] != "/":
                        urls_to_scrape[0] = "/" + \
                            urls_to_scrape[0]
                    try:
                        r = requests.get(
                            url + urls_to_scrape[0])
                        soup = BeautifulSoup(r.text, 'html.parser')
                        tags = soup.find_all('a')
                    except Exception as e:
                        print(e)

                urls_to_scrape.remove(urls_to_scrape[0])
            else:
                print(urls_to_scrape)
                run = False

    except KeyboardInterrupt:
        run = False
