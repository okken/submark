"""
"""

import re


def headers(line):
    line = re.sub(r"^# (.*)", r"<h1> \1 </h1>", line)
    line = re.sub(r"^## (.*)", r"<h2> \1 </h2>", line)
    line = re.sub(r"^### (.*)", r"<h3> \1 </h3>", line)
    line = re.sub(r"^#### (.*)", r"<h4> \1 </h4>", line)
    line = re.sub(r"^##### (.*)", r"<h5> \1 </h5>", line)
    return line


def strong(line):
    line = re.sub(r"\*\*(.*)\*\*", r"<strong>\1</strong>", line)
    line = re.sub(r"__(.*)__", r"<strong>\1</strong>", line)
    return line


def em(line):
    line = re.sub(r"\*(.*)\*", r"<em>\1</em>", line)
    line = re.sub(r"_(.*)_", r"<em>\1</em>", line)
    return line


def convert_line(line):
    line = line.rstrip()
    line = headers(line)
    line = strong(line)
    line = em(line)
    return line


def convert_list(lines):
    converted_list = [convert_line(l) for l in lines]
    return "\n".join(converted_list)


def convert(some_string):
    return convert_list(some_string.split("\n"))
