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


def link(line):
    line = re.sub(r'\[(.+)\]\(([^ ]+) (".+")\)',
                  r'<a href="\2" title=\3>\1</a>',
                  line)
    line = re.sub(r'\[(.+)\]\(([^ ]+)\)',
                  r'<a href="\2">\1</a>',
                  line)
    return line


def image(line):
    # example: r'![alt](/some/image.png) "title")',
    #     out: r'<img src="/some/image.png" alt="alt" title="title"/>',
    line = re.sub(r'!\[(.+)\]\(([^ ]+) "(.+)"\)',
                  r'<img src="\2" alt="\1" title="\3"/>',
                  line)
    return line


def code_span(line):
    # example: this is `some code`
    #     out: this is <code>some code</code>
    line = re.sub(r'`([^`]+)`', r'<code>\1</code>', line)
    return line


def horizontal_rule(line):
    # example: ---
    #     out: <hr/>
    line = re.sub(r'^---+ *$', r'<hr/>', line)
    return line


def line_break(line):
    # example: some text <then two spaces>
    #     out: some text<br/>
    line = re.sub(r'\s\s$', r' <br>', line)
    return line


def convert_line(line):
    line = line.rstrip('\n')
    line = headers(line)
    line = strong(line)
    line = em(line)
    line = image(line)
    line = link(line)
    line = code_span(line)
    line = horizontal_rule(line)
    line = line_break(line)
    return line


def convert_list(lines):
    converted_list = [convert_line(l) for l in lines]
    return "\n".join(converted_list)


def convert(some_string):
    return convert_list(some_string.split("\n"))
