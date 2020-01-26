from core.command_core import commands, register
import os
import sys
import importlib.util
import json
from colorama import Fore


@register("exit", "Used to exit the shell.", "Usage: exit")
def command_exit(shell, input):
    shell.shell_running = False


@register("load", "Used to load payload.", "Usage: load payloadname")
def command_load(shell, user_input):
    if user_input[1] in os.listdir("payloads"):
        shell.current_payload = user_input[1]
        spec = importlib.util.spec_from_file_location(
            f"{user_input[1]}", f"payloads/{user_input[1]}/payload.py")
        module = importlib.util.module_from_spec(spec)
        print(module)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        payload = getattr(module, "main")
        with open('payloads/'+user_input[1]+"/options.json", "r") as f:
            options = json.load(f)
        shell.payload_options = options["Params"][0]
        shell.payload_type = options["Type"]
        shell.payload = payload
        print(f"{Fore.BLUE}Payload: [{user_input[1]}] loaded.")
    else:
        print(f"{user_input[1]} not a valid payload.")


@register("options", "used to display payload options.", "Usage: options")
def command_options(shell, user_input):
    for keys, values in shell.payload_options.items():
        if type(values) == list:
            print(
                f"{Fore.BLUE}{keys} {Fore.GREEN}{str(values[0])} {Fore.RED} [{values[1]}]")
        else:
            print(f"{Fore.BLUE}{keys} {Fore.GREEN}{str(values)}")


@register("set", "Used to set payload options.", "Usage: set optionname value")
def command_set(shell, user_in):
    if len(user_in) > 2:
        shell.payload_options[user_in[1]][0] = user_in[2]
    else:
        print(f"{Fore.YELLOW}Incorrect usage. refeer to the help command.")


@register("shoot", "Used to launch the payload.", "Usage: shoot")
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
    results = shell.payload(arguments)
    if results:
        shell.results = results


@register("payloads", "shows all of the payloads currently in the payloads directory.", "Usage: payloads")
def command_payloads(shell, user_in):
    payload_list = os.listdir("payloads")
    if "__pycache__" in payload_list:
        payload_list.remove("__pycache__")
    payload_list.remove("word_lists")
    for i in payload_list:
        current_payload = os.listdir("payloads/"+i)
        with open('payloads/'+i+"/options.json", "r") as f:
            data = json.load(f)
        payload_name = data["Name"]
        help_text = data["HelpText"]
        print(
            f"{Fore.BLUE}Payload: [{payload_name}] {Fore.GREEN}Information: {help_text}")


@register("help", "help command.", "Usage: help commandname")
def command_help(shell, user_in):
    if len(user_in) > 1:
        if user_in[1] in commands:
            print(
                f"{Fore.BLUE}{commands[user_in[1]].helpmsg} {Fore.GREEN}[{commands[user_in[1]].usage}]")


@register("commands", "Shows all shell commands.", "Usage: commands")
def command_commands(shell, user_in):
    for key, values in commands.items():
        print(
            f"{Fore.BLUE}Command: ({key}) {Fore.GREEN}{commands[key].helpmsg}")


@register("write", "Writes output to a file.", "Usage: write filename")
def command_write(shell, user_in):
    if len(user_in) > 1:
        os.makedirs(os.path.dirname("output/"), exist_ok=True)
        results = shell.results
        with open("output/"+user_in[1]+".txt", 'w+', encoding="utf-8") as f:
            for i in results:
                f.write(str(i) + "\n")
        print(f"{Fore.BLUE} Urls Written too {Fore.GREEN} output/{user_in[1]}")
    else:
        print(f"{Fore.YELLOW}Incorrect Usage, please refeer to the help command.")


@register("update", "Updates the to the newest version of aawt using git.", "Usage: update")
def command_update(shell, user_in):
    os.system("git pull origin master")
