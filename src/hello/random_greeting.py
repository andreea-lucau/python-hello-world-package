"Say a random hello."

import random

from hello.greeting import is_valid_name

class Error(Exception):
    """Module-specific exception class."""
    pass


def get_random_greeting(name):
    """Get a random hello for the given name.

    The name is first validated - it has to be characters-only and non-empty.
    If the name is valid, read a data file with possible greetings, select one
    randomly and personalize it with the name.

    Args:
        name: string, the person to say hello to
    Returns:
        string, the hello
    """
    if not is_valid_name(name):
        raise Error("Name '%s' is not valid" % name)

    with open("greeting_templates.txt") as handle:
        templates = handle.readlines()

    template_index = random.randint(0, len(templates))
    return templates[template_index] % name
