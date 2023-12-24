import pytest

from conftest import assert_bash_exec, bash_env_saved


@pytest.mark.bashcomp(
    cmd=None,
    cwd="_filedir",
    ignore_env=r"^\+declare -f __tester$",
)
class TestDequote:
    def test_1_char(self, bash):
        assert_bash_exec(
            bash,
            '__tester() { local REPLY=dummy v=var;_comp_dequote "$1";local ext=$?;((${#REPLY[@]}))&&printf \'<%s>\' "${REPLY[@]}";echo;return $ext;}',
        )
        output = assert_bash_exec(bash, "__tester a", want_output=True)
        assert output.strip() == "<a>"

    def test_2_str(self, bash):
        output = assert_bash_exec(bash, "__tester abc", want_output=True)
        assert output.strip() == "<abc>"

    def test_3_null(self, bash):
        output = assert_bash_exec(bash, "__tester ''", want_output=True)
        assert output.strip() == ""

    def test_4_empty(self, bash):
        output = assert_bash_exec(bash, "__tester \"''\"", want_output=True)
        assert output.strip() == "<>"

    def test_5_brace(self, bash):
        output = assert_bash_exec(bash, "__tester 'a{1..3}'", want_output=True)
        assert output.strip() == "<a1><a2><a3>"

    def test_6_glob(self, bash):
        output = assert_bash_exec(bash, "__tester 'a?b'", want_output=True)
        assert output.strip() == "<a b><a$b><a&b><a'b>"

    def test_7_quote_1(self, bash):
        output = assert_bash_exec(
            bash, "__tester '\"a\"'\\'b\\'\\$\\'c\\'", want_output=True
        )
        assert output.strip() == "<abc>"

    def test_7_quote_2(self, bash):
        output = assert_bash_exec(
            bash, "__tester '\\\"\\'\\''\\$\\`'", want_output=True
        )
        assert output.strip() == "<\"'$`>"

    def test_7_quote_3(self, bash):
        output = assert_bash_exec(
            bash, "__tester \\$\\'a\\\\tb\\'", want_output=True
        )
        assert output.strip() == "<a\tb>"

    def test_7_quote_4(self, bash):
        output = assert_bash_exec(
            bash, '__tester \'"abc\\"def"\'', want_output=True
        )
        assert output.strip() == '<abc"def>'

    def test_7_quote_5(self, bash):
        output = assert_bash_exec(
            bash, "__tester \\'abc\\'\\\\\\'\\'def\\'", want_output=True
        )
        assert output.strip() == "<abc'def>"

    def test_8_param_1(self, bash):
        output = assert_bash_exec(bash, "__tester '$v'", want_output=True)
        assert output.strip() == "<var>"

    def test_8_param_2(self, bash):
        output = assert_bash_exec(bash, "__tester '${v}'", want_output=True)
        assert output.strip() == "<var>"

    def test_8_param_3(self, bash):
        output = assert_bash_exec(bash, "__tester '${#v}'", want_output=True)
        assert output.strip() == "<3>"

    def test_8_param_4(self, bash):
        output = assert_bash_exec(bash, "__tester '${v[0]}'", want_output=True)
        assert output.strip() == "<var>"

    def test_9_qparam_1(self, bash):
        output = assert_bash_exec(bash, "__tester '\"$v\"'", want_output=True)
        assert output.strip() == "<var>"

    def test_9_qparam_2(self, bash):
        output = assert_bash_exec(
            bash, "__tester '\"${v[@]}\"'", want_output=True
        )
        assert output.strip() == "<var>"

    def test_10_pparam_1(self, bash):
        output = assert_bash_exec(bash, "__tester '$?'", want_output=True)
        assert output.strip() == "<0>"

    def test_10_pparam_2(self, bash):
        output = assert_bash_exec(bash, "__tester '${#1}'", want_output=True)
        assert output.strip() == "<5>"  # The string `${#1}` is five characters

    def test_unsafe_1(self, bash):
        output = assert_bash_exec(
            bash, "! __tester '$(echo hello >&2)'", want_output=True
        )
        assert output.strip() == ""

    def test_unsafe_2(self, bash):
        output = assert_bash_exec(
            bash, "! __tester '|echo hello >&2'", want_output=True
        )
        assert output.strip() == ""

    def test_unsafe_3(self, bash):
        output = assert_bash_exec(
            bash, "! __tester '>| important_file.txt'", want_output=True
        )
        assert output.strip() == ""

    def test_unsafe_4(self, bash):
        output = assert_bash_exec(
            bash, "! __tester '`echo hello >&2`'", want_output=True
        )
        assert output.strip() == ""

    def test_glob_default(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.shopt("failglob", False)
            bash_env.shopt("nullglob", False)
            output = assert_bash_exec(
                bash, "__tester 'non-existent-*.txt'", want_output=True
            )
            assert output.strip() == "<non-existent-*.txt>"

    def test_glob_noglob(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.set("noglob", True)
            output = assert_bash_exec(
                bash,
                "__tester 'non-existent-*.txt'",
                want_output=True,
            )
            assert output.strip() == "<non-existent-*.txt>"

    def test_glob_failglob(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.shopt("failglob", True)
            output = assert_bash_exec(
                bash, "! __tester 'non-existent-*.txt'", want_output=True
            )
            assert output.strip() == ""

    def test_glob_nullglob(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.shopt("nullglob", True)
            output = assert_bash_exec(
                bash, "__tester 'non-existent-*.txt'", want_output=True
            )
            assert output.strip() == ""
