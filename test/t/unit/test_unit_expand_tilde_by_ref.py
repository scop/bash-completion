import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^[+-]var=")
class TestUnitExpandTildeByRef:
    def test_1(self, bash):
        assert_bash_exec(bash, "__expand_tilde_by_ref >/dev/null")

    def test_2(self, bash):
        """Test environment non-pollution, detected at teardown."""
        assert_bash_exec(
            bash,
            '_x() { local aa="~"; __expand_tilde_by_ref aa; }; _x; unset _x',
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
    def test_expand(self, bash, user_home, plain_tilde, suffix_expanded):
        user, home = user_home
        suffix, expanded = suffix_expanded
        if plain_tilde:
            user = ""
            if not suffix or not expanded:
                home = "~"
        elif not expanded:
            home = "~%s" % user
        output = assert_bash_exec(
            bash,
            r'var="~%s%s"; __expand_tilde_by_ref var; printf "%%s\n" "$var"'
            % (user, suffix),
            want_output=True,
        )
        assert output.strip() == "%s%s" % (home, suffix.replace(r"\$", "$"),)
