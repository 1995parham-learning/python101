from typing import Callable, Any


def repl(input_fn: Callable[[Any], str] = input) -> None:
    """
    repl reads user input and in the default case it uses the builtin
    input function but for automated testing it accepts an optional input_fn
    parameter
    """
    print(input_fn("mara-01> "))


def fake_input(prompt: Any) -> str:
    return "a fake input"


if __name__ == "__main__":
    repl()
    repl(fake_input)
