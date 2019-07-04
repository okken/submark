"""
"""


from .submark import convert_list
import fileinput


def main():
    print(convert_list(fileinput.input()))
