import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None)
class TestUnitExpandTilde:
    def test_1(self, bash):
        """The old interface `__expand_tilde_by_ref` should not fail when it is
        called without arguments"""
        assert_bash_exec(bash, "__expand_tilde_by_ref >/dev/null")

    def test_2(self, bash):
        """Test environment non-pollution, detected at teardown."""
        assert_bash_exec(
            bash,
            '_x() { local REPLY; _comp_expand_tilde "~"; }; _x; unset -f _x',
        )

    @pytest.fixture(scope="class")
    def functions(self, bash):
        # $HOME tinkering: protect against $HOME != ~user; our "home" is the
        # latter but plain_tilde follows $HOME
        assert_bash_exec(
            bash,
            '_comp__test_unit() { local REPLY HOME=$1; _comp_expand_tilde "$2"; printf "%s\\n" "$REPLY"; }',
        )

    @pytest.mark.parametrize("plain_tilde", (True, False))
    @pytest.mark.parametrize(
        "suffix_expanded",
        (
            ("", True),
            ("/foo", True),
            (r"/\$HOME", True),
            ("/a  b", True),
            ("/*", True),
            (";echo hello", False),
            ("/a;echo hello", True),
        ),
    )
    def test_expand(
        self, bash, user_home, plain_tilde, suffix_expanded, functions
    ):
        user, home = user_home
        suffix, expanded = suffix_expanded
        home2 = home
        if plain_tilde:
            user = ""
            if not suffix or not expanded:
                home2 = "~"
        elif not expanded:
            home2 = "~%s" % user
        output = assert_bash_exec(
            bash,
            r'_comp__test_unit "%s" "~%s%s"' % (home, user, suffix),
            want_output=True,
        )
        assert output.strip() == "%s%s" % (home2, suffix.replace(r"\$", "$"))
