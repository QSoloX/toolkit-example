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
        payload = getattr(module, "payload")
        shell.payload_options = options
        shell.payload = payload


@register("options", "used to display payload options")
def command_options(shell, user_input):
    for keys, values in shell.payload_options.items():
        print(keys + " " + str(values))


@register("set", "Used to set payload options")
def command_set(shell, user_input):
    shell.payload_options[user_input[1]][0] = user_input[2]


@register("shoot", "Used to launch the payload")
def command_shoot(shell, user_in):
    shell.payload(shell.payload_options["url"][0])


@register("payloads", "shows all of the payloads currently in payloads/")
def command_payloads(shell, user_in):
    print(os.listdir("payloads"))


@register("iloveyou", "used to show some love")
def command_iloveyou(shell, user_input):
    print("i love you " + user_input[1])
