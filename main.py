from arg_parser import args
from send_requests import r
from term_colors import bcolors
from py_crawler import PyCrawler
import os


def main():
    #  Welcome Message
    print(bcolors.BOLD + bcolors.HEADER +
          "AAWT (Almost A Web Toolkit)" + bcolors.ENDC)
    print(bcolors.WARNING + "This is a simple program written by QSoloX." + bcolors.ENDC)

    # Check Args and execute
    if args.type == "get" and not args.crawl:
        print(f"{bcolors.OKGREEN}{r.GET(args.url)}{bcolors.ENDC}")
    elif args.crawl > 0:
        crawler = PyCrawler(args.url)
        if args.crawl == 1:
            crawler.web_scrap_crawl()
        elif args.crawl == 2:
            crawler.word_list_crawl()
            crawler.web_scrap_crawl()
            if args.output:
                os.makedirs(os.path.dirname("output/"), exist_ok=True)
                with open("output/" + args.output, 'w+', encoding="utf-8") as f:
                    for i in crawler.results:
                        f.write(str(i) + "\n")


if __name__ == "__main__":
    main()
