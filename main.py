from arg_parser import args
from send_requests import r
from term_colors import bcolors
from py_crawler import PyCrawler
import os


def write_to_file(crawler, filename, input_tag=False):
    os.makedirs(os.path.dirname("output/"), exist_ok=True)
    with open("output/" + args.output, 'w+', encoding="utf-8") as f:
        for i in crawler.results:
            f.write(str(i) + "\n")
        print(
            f"{bcolors.OKBLUE} Urls written to output/{args.output} {bcolors.ENDC}")
    if input_tag:
        with open("output/input-" + args.output, 'w+', encoding="utf-8") as f:
            for i in crawler.input:
                f.write(str(i) + "\n")
            print(
                f"{bcolors.OKBLUE} Urls with input written to output/input-{args.output} {bcolors.ENDC}")


def main():
    #  Welcome Message
    print(bcolors.BOLD + bcolors.HEADER +
          "AAWT (Almost A Web Toolkit)" + bcolors.ENDC)
    print(bcolors.WARNING + "This is a simple program written by QSoloX." + bcolors.ENDC)

    # Check Args and execute
    if args.type == "get" and args.crawl == 0:
        print(f"{bcolors.OKGREEN}{r.GET(args.url)}{bcolors.ENDC}")
    elif args.crawl > 0:
        crawler = PyCrawler(args.url)
        if args.crawl == 1:
            crawler.web_scrap_crawl()
            if args.output:
                write_to_file(crawler, args.output)
        elif args.crawl == 2:
            crawler.word_list_crawl(args.list)
            crawler.web_scrap_crawl()
            if args.output:
                write_to_file(crawler, args.output)
        elif args.crawl == 3:
            crawler.word_list_crawl(args.list)
            crawler.web_scrap_crawl(True)
            if args.output:
                if crawler.input:
                    write_to_file(crawler, args.output, True)
                else:
                    write_to_file(crawler, args.output)


if __name__ == "__main__":
    main()
