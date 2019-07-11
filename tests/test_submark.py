import submark
import pytest
from subprocess import Popen, PIPE, STDOUT
from pytest import param


@pytest.mark.parametrize(
    "line, expected",
    [
        param("# h1", "<h1> h1 </h1>", id="#_h1"),
        param("## h2", "<h2> h2 </h2>", id="##_h2"),
        param("### h3", "<h3> h3 </h3>", id="###_h3"),
        param("#### h4", "<h4> h4 </h4>", id="####_h4"),
        param("##### h5", "<h5> h5 </h5>", id="#####_h5"),
        param("**strong**", "<strong>strong</strong>", id="**strong**"),
        param("__strong__", "<strong>strong</strong>", id="__strong__"),
        param("*em*", "<em>em</em>", id="*em*"),
        param("_em_", "<em>em</em>", id="_em_"),
    ],
)
def test_convert(line, expected):
    assert submark.convert(line) == expected


@pytest.mark.parametrize(
    "line, expected",
    [
        param(r'[message](http://some.link.html)',
              r'<a href="http://some.link.html">message</a>',
              id="normal_link"),
        param(r'[message](http://some.link.html "my title")',
              r'<a href="http://some.link.html" title="my title">message</a>',
              id="link_with_title"),
        param(r'![alt](/some/image.png "title")',
              r'<img src="/some/image.png" alt="alt" title="title"/>',
              id="image"),
        param(r"this is `some code`",
              r"this is <code>some code</code>",
              id="code_span"),
        param(r"`some code` and `more code`",
              r"<code>some code</code> and <code>more code</code>",
              id="two_code_spans"),
        param(r"some text  ",
              r"some text <br>",
              id="line_break"),
        param(r"---", r"<hr/>", id="hr3"),
        param(r"----", r"<hr/>", id="hr4"),
        param(r"-----   ", r"<hr/>", id="hr_with_spaces")
    ],
)
def test_convert_new_stuff(line, expected):
    assert submark.convert(line) == expected


def test_command_line_with_pipe():
    """
    Simulate: echo '**strong**' | submark
    """
    input_text = "**strong**"
    expected = "<strong>strong</strong>"

    pipe = Popen(["submark"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    output = pipe.communicate(input=input_text.encode("utf-8"))[0]
    actual = output.rstrip().decode("utf-8")

    assert actual == expected
