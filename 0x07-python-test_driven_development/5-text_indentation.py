#!/usr/bin/python3
"""Module dealing with ., ? and :"""


def text_indentation(text):
    """prints a text with 2 new lines after each of the char"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""

    for i, char in enumerate(text):
        if char == "\n":
            indent = ""
        elif char in ".?:":
            indent = char + "\n\n"
        else:
            indent = char

        result += indent

    # Remove spaces after ".?:\n\n"
    modified_result = ""
    idx = 0
    while idx < len(result):
        if result[idx:idx + 3] in (".\n\n", "?\n\n", ":\n\n"):
            modified_result += result[idx]
            modified_result += result[idx + 1]
            modified_result += result[idx + 2]
            idx += 3
            while idx < len(result) and result[idx] == " ":
                idx += 1
        else:
            modified_result += result[idx]
            idx += 1

    print(modified_result, end="")
