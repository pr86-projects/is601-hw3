import os
import multiprocessing
import pkgutil
import importlib

from app.commands import CommandHandler
from app.commands import Command
from dotenv import load_dotenv
import logging
import logging.config

class App:
    def __init__(self): # Constructor
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'TESTING')
        self.command_handler = CommandHandler()
        self.exit_event = multiprocessing.Event()  # Initialization of exit_event

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings
    
    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)

    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):  # Assuming a BaseCommand class exists
                            self.command_handler.register_command(plugin_name, item())
                            logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore
                    except ImportError as e:
                        logging.error(f"Error importing plugin {plugin_name}: {e}")

    def execute_command_in_process(self, command_name: str, *args):
        if command_name == 'exit':
            self.exit_event.set()  # Directly set the event for the exit command
            logging.info(f"Exit event set by command '{command_name}'.")
            return
        try:
            #Execute the command in a separate process
            process = multiprocessing.Process(target=self.command_handler.commands[command_name].execute, args=args)
            process.start()
            process.join(timeout=1)  # Wait for a short time for the process to complete
            if process.is_alive():
                process.terminate()  # Terminate the process if it's still alive after the timeout
        except KeyError:
            print(f"No such command: {command_name}")
            logging.error(f"No such command: {command_name}")

    def start(self):
        # Register commands here
        self.load_plugins()
        logging.info("Application started. Type 'exit' to exit.")
        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            #self.command_handler.execute_command(input(">>> ").strip())
            user_input = input(">>> ").strip()
            if not user_input:
                continue  # Skip empty input
            command_parts = user_input.split()
            command = command_parts[0]
            arguments = command_parts[1:]

            #if command == 'exit':  # Handle the 'exit' command directly
            #    print("Exiting...")
            #    break  # Break out of the loop to exit the application

            self.execute_command_in_process(command, *arguments)
            if self.exit_event.is_set():
                break  # Exit the loop if the exit event is set

        logging.info("Application exit.")
        print("Exiting application...")  # This line executes after the loop exits
