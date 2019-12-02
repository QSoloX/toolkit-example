
commands = {}


class Command:
    def __init__(self, name, helpmsg, func):
        self.name = name
        self.func = func
        self.helpmsg = helpmsg


def register(name, helpmsg):
    def inner(func):
        command = Command(name, helpmsg, func)
        commands[name] = command
    return inner


def command_notfound():
    print("command not found")


notfound = Command(None, None, command_notfound)
