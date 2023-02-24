import pytest

from conftest import assert_bash_exec, bash_env_saved


@pytest.mark.bashcomp(cmd=None)
class TestUtilCompgen:
    @pytest.fixture
    def functions(self, bash):
        assert_bash_exec(
            bash,
            "_comp__test_dump() { ((${#arr[@]})) && printf '<%s>' \"${arr[@]}\"; echo; }",
        )
        assert_bash_exec(
            bash,
            '_comp__test_words() { local -a arr=(00) input; input=("${@:1:$#-1}"); _comp_compgen arr -W \'${input[@]+"${input[@]}"}\' -- "${@:$#}"; _comp__test_dump; }',
        )
        assert_bash_exec(
            bash,
            '_comp__test_words_ifs() { local -a arr=(00); local input=$2; _comp_compgen -F "$1" arr -W \'$input\' -- "${@:$#}"; _comp__test_dump; }',
        )

    def test_1_basic(self, bash, functions):
        output = assert_bash_exec(
            bash, "_comp__test_words 12 34 56 ''", want_output=True
        )
        assert output.strip() == "<12><34><56>"

    def test_2_space(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "_comp__test_words $'a b' $'c d\\t' '  e  ' $'\\tf\\t' ''",
            want_output=True,
        )
        assert output.strip() == "<a b><c d\t><  e  ><\tf\t>"

    def test_2_IFS(self, bash, functions):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable("IFS", "34")
            output = assert_bash_exec(
                bash, "_comp__test_words 12 34 56 ''", want_output=True
            )
            assert output.strip() == "<12><34><56>"

    def test_3_glob(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "_comp__test_words '*' '[a-z]*' '[a][b][c]' ''",
            want_output=True,
        )
        assert output.strip() == "<*><[a-z]*><[a][b][c]>"

    def test_3_failglob(self, bash, functions):
        with bash_env_saved(bash) as bash_env:
            bash_env.shopt("failglob", True)
            output = assert_bash_exec(
                bash,
                "_comp__test_words '*' '[a-z]*' '[a][b][c]' ''",
                want_output=True,
            )
            assert output.strip() == "<*><[a-z]*><[a][b][c]>"

    def test_3_nullglob(self, bash, functions):
        with bash_env_saved(bash) as bash_env:
            bash_env.shopt("nullglob", True)
            output = assert_bash_exec(
                bash,
                "_comp__test_words '*' '[a-z]*' '[a][b][c]' ''",
                want_output=True,
            )
            assert output.strip() == "<*><[a-z]*><[a][b][c]>"

    def test_4_empty(self, bash, functions):
        output = assert_bash_exec(
            bash, "_comp__test_words ''", want_output=True
        )
        assert output.strip() == ""

    def test_5_option_F(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "_comp__test_words_ifs '25' ' 123 456 555 ' ''",
            want_output=True,
        )
        assert output.strip() == "< 1><3 4><6 >< >"
