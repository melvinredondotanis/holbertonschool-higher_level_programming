#!/usr/bin/python3

def append_write(filename="", text=""):
    """ Appends a text to a file (UTF8). """
    with open(filename, 'a') as f:
        f.write(text)
