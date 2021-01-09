#!/usr/bin/python3
"""
This is the module for
    text indentation
"""


def text_indentation(text):
    """
       text_indentation
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    [i.strip for i in text.split(".")]
    text = text.replace(". ", ".\n\n")
    text = text.replace(".", ".\n\n")
    [i.strip for i in text.split("?")]
    text = text.replace("? ", "?\n\n")
    text = text.replace("?", "?\n\n")
    [i.strip for i in text.split(":")]
    text = text.replace(": ", ":\n\n")
    text = text.replace(":", ":\n\n")
    print(text)
