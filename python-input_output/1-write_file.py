#!/usr/bin/python3
"""Writes a text to a file (UTF8)."""

def write_file(filename="", text=""):
    """
    Writes a text to a file (UTF8).
    """
    with open(filename) as f:
        f.write(text)
