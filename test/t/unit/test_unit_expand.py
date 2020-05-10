import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^[+-](cur|COMPREPLY)=")
class TestUnitExpand:
    def test_1(self, bash):
        assert_bash_exec(bash, "_expand >/dev/null")

    def test_2(self, bash):
        """Test environment non-pollution, detected at teardown."""
        assert_bash_exec(bash, "foo() { _expand; }; foo; unset foo")

    def test_user_home_compreply(self, bash, user_home):
        user, home = user_home
        output = assert_bash_exec(
            bash,
            r'cur="~%s"; _expand; printf "%%s\n" "$COMPREPLY"' % user,
            want_output=True,
        )
        assert output.strip() == home

    def test_user_home_cur(self, bash, user_home):
        user, home = user_home
        output = assert_bash_exec(
            bash,
            r'cur="~%s/a"; _expand; printf "%%s\n" "$cur"' % user,
            want_output=True,
        )
        assert output.strip() == "%s/a" % home
