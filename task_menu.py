from abc import ABCMeta, abstractmethod


class CommandException(Exception):
    pass

class Command(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        """Execute the command."""


class Menu:
    def __init__(self):
        self.commands = {}
        self.counter = 0

    def add_command(self, name, klass):
        if not name:
            raise CommandException('Command must have a name')
        if not issubclass(klass, Command):
            raise CommandException(f'Class "{klass}" is not Command')

        self.commands[name] = klass

    def execute(self, name, *args, **kwargs):
        if name not in self.commands:
            raise CommandException(f'Command with name "{name}" not found')
        return self.commands[name](*args, **kwargs).execute()

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.commands):
            result = tuple(enumerate(self.commands))
            command_name = result[self.counter][1]
            command_class = self.commands[command_name]
            self.counter += 1
            return command_name, command_class
        else:
            raise StopIteration

