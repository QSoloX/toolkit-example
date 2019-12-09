# from arg_parser import args
from colorama import init, deinit, Fore
# from send_requests import r
# from term_colors import bcolors
# from py_crawler import PyCrawler
from core.command_shell import Shell
import os
import platform
init()


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
