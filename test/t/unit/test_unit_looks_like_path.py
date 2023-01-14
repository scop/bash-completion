import shlex

import pytest

from conftest import TestUnitBase, assert_bash_exec


@pytest.mark.bashcomp(cmd=None)
class TestUnitQuote(TestUnitBase):
    @pytest.mark.parametrize(
        "thing_looks_like",
        (
            ("", False),
            ("foo", False),
            ("/foo", True),
            ("foo/", True),
            ("foo/bar", True),
            (".", True),
            ("../", True),
            ("~", True),
            ("~foo", True),
        ),
    )
    def test_1(self, bash, thing_looks_like):
        thing, looks_like = thing_looks_like
        output = assert_bash_exec(
            bash,
            f"_comp_looks_like_path {shlex.quote(thing)}; printf %s $?",
            want_output=True,
            want_newline=False,
        )
        is_zero = output.strip() == "0"
        assert (looks_like and is_zero) or (not looks_like and not is_zero)
