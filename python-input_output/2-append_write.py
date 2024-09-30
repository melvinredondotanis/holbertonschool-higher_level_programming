#!/usr/bin/python3
"""Appends a text to a file (UTF8)."""


def append_write(filename="", text=""):
    """
    Appends a text to a file (UTF8).
    """
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
    return len(text)
