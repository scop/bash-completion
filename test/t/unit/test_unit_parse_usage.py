import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^\+declare -f fn$")
class TestUnitParseUsage:
    def test_1(self, bash):
        assert_bash_exec(bash, "fn() { echo; }")
        output = assert_bash_exec(bash, "_parse_usage fn")
        assert not output

    def test_2(self, bash):
        assert_bash_exec(bash, "fn() { echo 'no dashes here'; }")
        output = assert_bash_exec(bash, "_parse_usage fn")
        assert not output

    def test_3(self, bash):
        assert_bash_exec(bash, "fn() { echo 'foo [-f]'; }")
        output = assert_bash_exec(bash, "_parse_usage fn", want_output=True)
        assert output.split() == "-f".split()

    def test_4(self, bash):
        assert_bash_exec(bash, "fn() { echo 'bar [-aBcD] [-e X]'; }")
        output = assert_bash_exec(bash, "_parse_usage fn", want_output=True)
        assert output.split() == "-a -B -c -D -e".split()

    def test_5(self, bash):
        assert_bash_exec(bash, "fn() { echo '[-[XyZ]] [--long=arg]'; }")
        output = assert_bash_exec(bash, "_parse_usage fn", want_output=True)
        assert output.split() == "-X -y -Z --long=".split()

    def test_6(self, bash):
        assert_bash_exec(bash, "fn() { echo '[-s|--long]'; }")
        output = assert_bash_exec(bash, "_parse_usage fn", want_output=True)
        assert output.split() == "--long".split()

    def test_7(self, bash):
        assert_bash_exec(bash, "fn() { echo '[-s, --long=arg]'; }")
        output = assert_bash_exec(bash, "_parse_usage fn", want_output=True)
        assert output.split() == "--long=".split()

    def test_8(self, bash):
        assert_bash_exec(bash, "fn() { echo '[--long/-s] [-S/--longer]'; }")
        output = assert_bash_exec(bash, "_parse_usage fn", want_output=True)
        assert output.split() == "--long --longer".split()

    def test_9(self, bash):
        assert_bash_exec(bash, "fn() { echo '[ -a ] [ -b foo ]'; }")
        output = assert_bash_exec(bash, "_parse_usage fn", want_output=True)
        assert output.split() == "-a -b".split()

    def test_10(self, bash):
        assert_bash_exec(bash, "fn() { echo '[ -a | --aa ]'; }")
        output = assert_bash_exec(bash, "_parse_usage fn", want_output=True)
        assert output.split() == "--aa".split()

    def test_11(self, bash):
        assert_bash_exec(
            bash, "fn() { echo ----; echo ---foo; echo '----- bar'; }"
        )
        output = assert_bash_exec(bash, "_parse_usage fn")
        assert not output

    def test_12(self, bash):
        output = assert_bash_exec(
            bash, "echo '[-duh]' | _parse_usage -", want_output=True
        )
        assert output.split() == "-d -u -h".split()
