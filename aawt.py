# from arg_parser import args
from colorama import init, deinit, Fore
# from send_requests import r
# from term_colors import bcolors
# from py_crawler import PyCrawler
from core.command_shell import Shell
import os
import platform
init()


# def write_to_file(crawler, filename, input_tag=False):
#     os.makedirs(os.path.dirname("output/"), exist_ok=True)
#     with open("output/" + args.output, 'w+', encoding="utf-8") as f:
#         for i in crawler.results:
#             f.write(str(i) + "\n")
#         print(
#             f"{bcolors.OKBLUE} Urls written to output/{args.output} {bcolors.ENDC}")
#     if input_tag:
#         with open("output/input-" + args.output, 'w+', encoding="utf-8") as f:
#             for i in crawler.input:
#                 f.write(str(i) + "\n")
#             print(
#                 f"{bcolors.OKBLUE} Urls with input written to output/input-{args.output} {bcolors.ENDC}")

def user_input_checker(user_in, shell_running):
    if user_in:
        # check dict?
        pass


def main():
    # Set needed variables
    shell_running = True
    current_payload = ""

    # Clear terminal
    if platform.system() == "Linux":
        os.system('clear')
    else:
        os.system('cls')

    #  Welcome Message
    print(f"{Fore.MAGENTA}AAWT (Almost A Web Toolkit)")
    print(f"{Fore.YELLOW}This is a simple program written by QSoloX.\n")

    # Load all needed files here

    shell = Shell()
    shell.run()


if __name__ == "__main__":
    main()
