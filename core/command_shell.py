from colorama import init, deinit, Fore
from core.commands import *


class Shell:
    def __init__(self):
        # Init colorama
        init()
        # shell variables
        self.current_payload = ""
        self.payload_options = {}
        self.payload_init = None
        self.payload_attack = None
        self.shell_running = True

    def run(self):
        while self.shell_running:
            try:
                print(
                    f"{Fore.CYAN}AAWT {self.current_payload}>{Fore.RED}", end=" ")
                user_in = input(f" ").split(" ")

                if user_in[0] in commands:
                    commands[user_in[0]].func(self, user_in)

            except KeyboardInterrupt:
                self.shell_running = False

    def execute_command(self, user_in):
        if user_in:
            print(user_in)
