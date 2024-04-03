import re

import pytest

from conftest import assert_bash_exec, assert_complete, bash_env_saved


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
            '_comp__test_compgen() { local -a arr=(00); _comp_compgen -v arr "$@"; _comp__test_dump; }',
        )
        assert_bash_exec(
            bash,
            '_comp__test_words() { local -a input=("${@:1:$#-1}"); _comp__test_compgen -c "${@:$#}" -- -W \'${input[@]+"${input[@]}"}\'; }',
        )
        assert_bash_exec(
            bash,
            '_comp__test_words_ifs() { local input=$2; _comp__test_compgen -F "$1" -c "${@:$#}" -- -W \'$input\'; }',
        )

        assert_bash_exec(
            bash,
            '_comp_cmd_fc() { _comp_compgen -c "$(_get_cword)" -C _filedir filedir; }; '
            "complete -F _comp_cmd_fc fc; "
            "complete -F _comp_cmd_fc -o filenames fc2",
        )
        assert_bash_exec(
            bash,
            '_comp_cmd_fcd() { _comp_compgen -c "$(_get_cword)" -C _filedir filedir -d; }; '
            "complete -F _comp_cmd_fcd fcd",
        )

        # test_8_option_U
        assert_bash_exec(
            bash,
            "_comp_compgen_gen8() { local -a arr=(x y z); _comp_compgen -U arr -- -W '\"${arr[@]}\"'; }",
        )

        # test_9_inherit_a
        assert_bash_exec(
            bash,
            '_comp_compgen_gen9sub() { local -a gen=(00); _comp_compgen -v gen -- -W 11; _comp_compgen_set "${gen[@]}"; }; '
            "_comp_compgen_gen9() { _comp_compgen_gen9sub; _comp_compgen -a gen9sub; }",
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

    def test_6_option_C_1(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "_comp__test_compgen -c a -C _filedir filedir",
            want_output=True,
        )
        set1 = set(re.findall(r"<[^<>]*>", output.strip()))
        assert set1 == {"<a b>", "<a$b>", "<a&b>", "<a'b>", "<ab>", "<aé>"}

    def test_6_option_C_2(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "_comp__test_compgen -c b -C _filedir -- -d",
            want_output=True,
        )
        assert output.strip() == "<brackets>"

    @pytest.mark.parametrize("funcname", "fc fc2".split())
    def test_6_option_C_3(self, bash, functions, funcname):
        completion = assert_complete(bash, "%s _filedir ab/" % funcname)
        assert completion == "e"

    @pytest.mark.complete(r"fcd a\ ")
    def test_6_option_C_4(self, functions, completion):
        # Note: we are not in the original directory that "b" exists, so Bash
        # will not suffix a slash to the directory name.
        assert completion == "b"

    def test_7_icmd(self, bash, functions):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable(
                "BASH_COMPLETION_USER_DIR", "$PWD/_comp_compgen", quote=False
            )

            completions = assert_complete(bash, "compgen-cmd1 '")
            assert completions == ["012", "123", "234", "5abc", "6def", "7ghi"]

    def test_7_xcmd(self, bash, functions):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable(
                "BASH_COMPLETION_USER_DIR", "$PWD/_comp_compgen", quote=False
            )

            completions = assert_complete(bash, "compgen-cmd2 '")
            assert completions == ["012", "123", "234", "5foo", "6bar", "7baz"]

    def test_8_option_U(self, bash, functions):
        output = assert_bash_exec(
            bash, "_comp__test_compgen gen8", want_output=True
        )
        assert output.strip() == "<x><y><z>"

    def test_9_inherit_a(self, bash, functions):
        output = assert_bash_exec(
            bash, "_comp__test_compgen gen9", want_output=True
        )
        assert output.strip() == "<11><11>"
