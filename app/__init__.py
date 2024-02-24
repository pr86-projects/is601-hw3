from app.commands import CommandHandler
from app.commands.discord import DiscordCommand
from app.commands.exit import ExitCommand
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand
from app.commands.menu import MenuCommand
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()


    def start(self):
        # Register commands here
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("menu", MenuCommand())
        self.command_handler.register_command("discord", DiscordCommand())
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())
    
        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            #self.command_handler.execute_command(input(">>> ").strip())
            user_input = input(">>> ").strip()
            if not user_input:
                continue  # Skip empty input
            command_parts = user_input.split()
            command = command_parts[0]
            arguments = command_parts[1:]
            self.command_handler.execute_command(command, *arguments)
