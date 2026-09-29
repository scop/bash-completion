import pytest

from conftest import assert_bash_exec, bash_env_saved


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^[+-](cur|COMPREPLY)=")
class TestUnitExpand:
    def test_1(self, bash):
        assert_bash_exec(bash, "_comp_expand >/dev/null")

    def test_2(self, bash):
        """Test environment non-pollution, detected at teardown."""
        assert_bash_exec(bash, "foo() { _comp_expand; }; foo; unset -f foo")

    def test_user_home_compreply(self, bash, user_home):
        user, home = user_home
        output = assert_bash_exec(
            bash,
            r'cur="~%s"; _comp_expand; printf "%%s\n" "$COMPREPLY"' % user,
            want_output=True,
        )
        assert output.strip() == home

    def test_user_home_compreply_failglob(self, bash, user_home):
        user, home = user_home
        with bash_env_saved(bash) as bash_env:
            bash_env.shopt("failglob", True)
            output = assert_bash_exec(
                bash,
                r'cur="~%s"; _comp_expand; printf "%%s\n" "$COMPREPLY"' % user,
                want_output=True,
            )
        assert output.strip() == home

    def test_user_home_cur(self, bash, user_home):
        user, home = user_home
        output = assert_bash_exec(
            bash,
            r'cur="~%s/a"; _comp_expand; printf "%%s\n" "$cur"' % user,
            want_output=True,
        )
        assert output.strip() == "%s/a" % home
