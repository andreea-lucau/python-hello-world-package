"""Say a simple hello."""

import sys


class Error(Exception):
    """Module-specific exception class."""
    pass


def is_valid_name(name):
    """Check if the given name is valid

    A name if consider valid if it is non-empty, contains only characters and
    the first letter is in uppercase.

    Args:
        name: string, the name to check for

    Returns:
        True if the name is valid, false otherwise
    """

    if not name:
        return False

    if not name[0].isupper():
        return False

    for char in name:
        if not char.isalpha():
            return False

    return True


def get_greeting(name):
    """Get a standard hello for the given name.

    The name is first validated - it has to be characters-only and non-empty.
    The hello is: Hello, <name>!

    Args:
        name: string, the person to say hello to
    Returns:
        the simple hello
    """

    if not is_valid_name(name):
        raise Error("Name '%s' is not valid" % name)

    return "Hello, " + name + "!"


def print_usage():
    """Usage for greeting.py script."""
    print "Usage:"
    print "./hello <name>"


def main():
    """The corresponding main function for the module."""
    if len(sys.argv) != 2:
        print "Invalid parameters!"
        print_usage()
        return

    print get_greeting(sys.argv[1])


if __name__ == "__main__":
    main()
