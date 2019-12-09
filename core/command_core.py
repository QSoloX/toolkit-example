
commands = {}


class Command:
    def __init__(self, name, helpmsg, usage, func):
        self.name = name
        self.func = func
        self.helpmsg = helpmsg
        self.usage = usage


def register(name, helpmsg, usage):
    def inner(func):
        command = Command(name, helpmsg, usage, func)
        commands[name] = command
    return inner


def command_notfound():
    print("command not found")


notfound = Command(None, None, None, command_notfound)
