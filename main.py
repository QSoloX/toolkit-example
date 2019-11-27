from arg_parser import args
from send_requests import r
from term_colors import bcolors
from py_crawler import PyCrawler


def main():
    #  Welcome Message
    print(bcolors.BOLD + bcolors.HEADER +
          "AAWT (Almost A Web Toolkit)" + bcolors.ENDC)
    print(bcolors.WARNING + "This is a simple program written by QSoloX." + bcolors.ENDC)

    # Check Args and execute
    if args.type == "get" and not args.crawl:
        print(f"{bcolors.OKGREEN}{r.GET(args.url)}{bcolors.ENDC}")
    elif args.crawl:
        crawler = PyCrawler(args.url)
        crawler.word_list_crawl()
        crawler.web_scrap_crawl()


if __name__ == "__main__":
    main()
