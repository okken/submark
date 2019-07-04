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
