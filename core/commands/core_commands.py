from core.command_core import commands, register
import os
from colorama import Fore


@register("exit", "Used to exit the shell.", "Usage: exit")
def command_exit(shell, input):
    shell.shell_running = False


@register("load", "Used to load payload.", "Usage: load payloadname")
def command_load(shell, user_input):
    if user_input[1] + ".py" in os.listdir("payloads"):
        shell.current_payload = user_input[1]
        module = __import__(f"payloads.{user_input[1]}")
        options = getattr(module, user_input[1]+"_options")
        payload = getattr(module, user_input[1])
        shell.payload_options = options
        shell.payload = payload
        print(f"{Fore.BLUE}Payload: [{user_input[1]}] loaded.")
    else:
        print(f"{user_input[1]} not a valid payload.")


@register("options", "used to display payload options", "Usage: options")
def command_options(shell, user_input):
    for keys, values in shell.payload_options.items():
        if len(values) > 1:
            print(
                f"{Fore.BLUE}{keys} {Fore.GREEN}{str(values[0])} {Fore.RED} [{values[1]}]")
        else:
            print(f"{Fore.BLUE}{keys} {Fore.GREEN}{str(values)}")


@register("set", "Used to set payload options", "Usage: set optionname value")
def command_set(shell, user_input):
    shell.payload_options[user_input[1]][0] = user_input[2]


@register("shoot", "Used to launch the payload", "Usage: shoot")
def command_shoot(shell, user_in):
    arguments = []
    for keys, values in shell.payload_options.items():
        if len(values) == 2:
            if values[0] == "":
                print(f"error required argument {keys} has no assigned value.")
                return
            else:
                arguments.append(values[0])
        else:
            arguments.append(values)
    if len(arguments) == 1:
        arguments = arguments[0]
    shell.payload(arguments)


@register("payloads", "shows all of the payloads currently in the payloads directory.", "Usage: payloads")
def command_payloads(shell, user_in):
    payload_list = os.listdir("payloads")
    payload_list.remove("__init__.py")
    payload_list.remove("__pycache__")
    payload_list.remove("word_lists")
    for i in payload_list:
        test = i.replace(".py", "")
        module = __import__(f"payloads.{test}")
        help_text = getattr(module, test+"_help_text")

        print(
            f"{Fore.BLUE}Payload: [{test}] {Fore.GREEN}Information: {help_text}")


@register("help", "help command.", "Usage: help commandname")
def command_help(shell, user_in):
    if len(user_in) > 1:
        print(
            f"{Fore.BLUE}{commands[user_in[1]].helpmsg} {Fore.GREEN}[{commands[user_in[1]].usage}]")
