from core.command_core import commands, register
import os


@register("exit()", "Used to exit the shell.")
def command_exit(shell, input):
    shell.shell_running = False


@register("load", "Used to load payload.")
def command_load(shell, user_input):
    if user_input[1] + ".py" in os.listdir("payloads"):
        shell.current_payload = user_input[1]
        module = __import__(f"payloads.{user_input[1]}")
        options = getattr(module, "options")
        payload_init = getattr(module, "payload_init")
        # payload_attack = getattr(module, "payload_attack")
        shell.payload_options = options
        shell.payload_init = payload_init
        # shell.payload_attack = payload_attack


@register("options", "used to display payload options")
def command_options(shell, user_input):
    for keys, values in shell.payload_options.items():
        print(keys + " " + str(values))


@register("set", "Used to set payload options")
def command_set(shell, user_input):
    shell.payload_options[user_input[1]] = user_input[2]


@register("shoot", "Used to launch the payload")
def command_shoot(shell, user_in):
    thing = shell.payload_init(shell.payload_options['url'])
    thing.attack(shell.payload_options['check_input'])


@register("payloads", "shows all of the payloads currently in payloads/")
def command_payloads(shell, user_in):
    print(os.listdir("payloads"))


@register("iloveyou", "used to show some love")
def command_iloveyou(shell, user_input):
    print("i love you " + user_input[1])
