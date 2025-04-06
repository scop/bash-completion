import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(
    cmd=None,
    cwd="_filedir",
    ignore_env=r"^\+declare -f __tester$",
)
class TestDequoteIncomplete:
    @pytest.fixture
    def functions(self, bash):
        assert_bash_exec(
            bash,
            '__tester() { local REPLY=dummy v=var;_comp_dequote_incomplete "$1";local ext=$?;((${#REPLY[@]}))&&printf \'<%s>\' "${REPLY[@]}";echo;return $ext;}',
        )

    def test_basic_1(self, bash, functions):
        output = assert_bash_exec(bash, "__tester a", want_output=True)
        assert output.strip() == "<a>"

    def test_basic_2(self, bash, functions):
        output = assert_bash_exec(bash, "__tester abc", want_output=True)
        assert output.strip() == "<abc>"

    def test_basic_3_null(self, bash, functions):
        output = assert_bash_exec(bash, "! __tester ''", want_output=True)
        assert output.strip() == ""

    def test_basic_4_empty(self, bash, functions):
        output = assert_bash_exec(bash, "__tester \"''\"", want_output=True)
        assert output.strip() == "<>"

    def test_basic_5_brace(self, bash, functions):
        output = assert_bash_exec(bash, "__tester 'a{1..3}'", want_output=True)
        assert output.strip() == "<a1><a2><a3>"

    def test_basic_6_glob(self, bash, functions):
        output = assert_bash_exec(bash, "__tester 'a?b'", want_output=True)
        assert output.strip() == "<a b><a$b><a&b><a'b>"

    def test_quote_1(self, bash, functions):
        output = assert_bash_exec(
            bash, "__tester '\"a\"'\\'b\\'\\$\\'c\\'", want_output=True
        )
        assert output.strip() == "<abc>"

    def test_quote_2(self, bash, functions):
        output = assert_bash_exec(
            bash, "__tester '\\\"\\'\\''\\$\\`'", want_output=True
        )
        assert output.strip() == "<\"'$`>"

    def test_quote_3(self, bash, functions):
        output = assert_bash_exec(
            bash, r"__tester \$\'a\\tb\'", want_output=True
        )
        assert output.strip() == "<a\tb>"

    def test_quote_4(self, bash, functions):
        output = assert_bash_exec(
            bash, '__tester \'"abc\\"def"\'', want_output=True
        )
        assert output.strip() == '<abc"def>'

    def test_quote_5(self, bash, functions):
        output = assert_bash_exec(
            bash, r"__tester \'abc\'\\\'\'def\'", want_output=True
        )
        assert output.strip() == "<abc'def>"

    def test_incomplete_1(self, bash, functions):
        output = assert_bash_exec(bash, r"__tester 'a\'", want_output=True)
        assert output.strip() == "<a>"

    def test_incomplete_2(self, bash, functions):
        output = assert_bash_exec(bash, '__tester "\'a b "', want_output=True)
        assert output.strip() == "<a b >"

    def test_incomplete_3(self, bash, functions):
        output = assert_bash_exec(bash, "__tester '\"a b '", want_output=True)
        assert output.strip() == "<a b >"
