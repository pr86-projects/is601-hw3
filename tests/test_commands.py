"""
This module contains tests for the all Commands.
"""
from app import App
from app.plugins.goodbye import GoodbyeCommand
from app.plugins.greet import GreetCommand
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand

def test_greet_command(capfd):
    """This test verifies that the GreetCommand class prints 'Hello, World!' when executed."""
    command = GreetCommand()
    command.execute()
    out, err = capfd.readouterr() # pylint: disable=unused-variable
    assert out == "Hello, World!\n", "The GreetCommand should print 'Hello, World!'"

def test_goodbye_command(capfd):
    """This test verifies that the GoodbyeCommand class prints 'Goodbye' when executed. """
    command = GoodbyeCommand()
    command.execute()
    out, err = capfd.readouterr() # pylint: disable=unused-variable
    assert out == "Goodbye\n", "The GreetCommand should print 'Hello, World!'"

def test_add_command(capfd):
    """This test verifies that the AddCommand class prints 'The result is: 10' when executed."""
    command = AddCommand()
    command.execute(2, 8)
    out, err = capfd.readouterr() # pylint: disable=unused-variable
    assert out == "The result is: 10\n", "The AddCommand should print 'The result is: 10'"

def test_subtract_command(capfd):
    """This test verifies that the SubtractCommand class prints 'The result is: -6' when executed."""
    command = SubtractCommand()
    command.execute(2, 8)
    out, err = capfd.readouterr() # pylint: disable=unused-variable
    assert out == "The result is: -6\n", "The SubtractCommand should print 'The result is: -6'"

def test_multiply_command(capfd):
    """This test verifies that the MultiplyCommand class prints 'The result is: 16' when executed."""
    command = MultiplyCommand()
    command.execute(2, 8)
    out, err = capfd.readouterr() # pylint: disable=unused-variable
    assert out == "The result is: 16\n", "The MultiplyCommand should print 'The result is: 16'"

def test_divide_command(capfd):
    """This test verifies that the DivideCommand class prints 'The result is: 4' when executed."""
    command = DivideCommand()
    command.execute(8, 2)
    out, err = capfd.readouterr() # pylint: disable=unused-variable
    assert out == "The result is: 4\n", "The DivideCommand should print 'The result is: 4'"

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    #with pytest.raises(SystemExit) as e:
    #    app.start()  # Assuming App.start() is now a static method based on previous discussions
    app.start()
    captured = capfd.readouterr()
    #assert str(e.value) == "Hello, World!", "The app did not exit as expected"
    assert "Hello, World!" in captured.out
    assert "Exiting application..." in captured.out

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    #with pytest.raises(SystemExit) as e:
    #    app.start()  # Assuming App.start() is now a static method based on previous discussions
    app.start()
    captured = capfd.readouterr()
    #assert str(e.value) == "Exiting...", "The app did not exit as expected"
    assert "Exiting application..." in captured.out
