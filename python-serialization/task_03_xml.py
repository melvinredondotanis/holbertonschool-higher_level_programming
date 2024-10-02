#!/usr/bin/python3
"""Converts a class to a XML string."""


def serialize_to_xml(dictionary, filename):
    """Serialize data to XML and save to file."""
    import xml.etree.ElementTree as ET
    root = ET.Element("root")
    for key, value in dictionary.items():
        ET.SubElement(root, key).text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Load data from file and deserialize from XML."""
    import xml.etree.ElementTree as ET
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    return dictionary
