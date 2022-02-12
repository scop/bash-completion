import pytest

from conftest import assert_bash_exec, bash_env_saved


@pytest.mark.bashcomp(
    cmd=None, ignore_env=r"^\+declare -f (dump_array|__tester)$"
)
class TestUtilSplit:
    @pytest.fixture
    def functions(self, bash):
        assert_bash_exec(
            bash, "dump_array() { printf '<%s>' \"${arr[@]}\"; echo; }"
        )
        assert_bash_exec(
            bash,
            '__tester() { local -a arr=(00); _comp_split "${@:1:$#-1}" arr "${@:$#}"; dump_array; }',
        )

    def test_1(self, bash, functions):
        output = assert_bash_exec(
            bash, "__tester '12 34 56'", want_output=True
        )
        assert output.strip() == "<12><34><56>"

    def test_2(self, bash, functions):
        output = assert_bash_exec(
            bash, "__tester $'12\\n34\\n56'", want_output=True
        )
        assert output.strip() == "<12><34><56>"

    def test_3(self, bash, functions):
        output = assert_bash_exec(
            bash, "__tester '12:34:56'", want_output=True
        )
        assert output.strip() == "<12:34:56>"

    def test_option_F_1(self, bash, functions):
        output = assert_bash_exec(
            bash, "__tester -F : '12:34:56'", want_output=True
        )
        assert output.strip() == "<12><34><56>"

    def test_option_F_2(self, bash, functions):
        output = assert_bash_exec(
            bash, "__tester -F : '12 34 56'", want_output=True
        )
        assert output.strip() == "<12 34 56>"

    def test_option_l_1(self, bash, functions):
        output = assert_bash_exec(
            bash, "__tester -l $'12\\n34\\n56'", want_output=True
        )
        assert output.strip() == "<12><34><56>"

    def test_option_l_2(self, bash, functions):
        output = assert_bash_exec(
            bash, "__tester -l '12 34 56'", want_output=True
        )
        assert output.strip() == "<12 34 56>"

    def test_option_a_1(self, bash, functions):
        output = assert_bash_exec(
            bash, "__tester -aF : '12:34:56'", want_output=True
        )
        assert output.strip() == "<00><12><34><56>"

    def test_protect_from_failglob(self, bash, functions):
        with bash_env_saved(bash) as bash_env:
            bash_env.shopt("failglob", True)
            output = assert_bash_exec(
                bash, "__tester -F '*' '12*34*56'", want_output=True
            )
            assert output.strip() == "<12><34><56>"

    def test_protect_from_nullglob(self, bash, functions):
        with bash_env_saved(bash) as bash_env:
            bash_env.shopt("nullglob", True)
            output = assert_bash_exec(
                bash, "__tester -F '*' '12*34*56'", want_output=True
            )
            assert output.strip() == "<12><34><56>"

    def test_protect_from_IFS(self, bash, functions):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable("IFS", "34")
            output = assert_bash_exec(
                bash, "__tester '12 34 56'", want_output=True
            )
            assert output.strip() == "<12><34><56>"
