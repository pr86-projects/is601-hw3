import sys
from app.commands import Command


class ExitCommand(Command):
    def execute(self):
        # Do not use sys.exit() as the App class handles the exit process
        #sys.exit("Exiting...")
        pass
        