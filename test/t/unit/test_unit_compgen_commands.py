import pytest

from conftest import assert_bash_exec, assert_complete, bash_env_saved


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^\+COMPREPLY=")
class TestUtilCompgenCommands:
    @pytest.fixture(scope="class")
    def functions(self, request, bash):
        assert_bash_exec(
            bash,
            r"_comp_compgen_commands__test() {"
            r"    local COMPREPLY=() cur=${1-};"
            r"    _comp_compgen_commands;"
            r'    printf "%s\n" "${COMPREPLY[@]-}";'
            r"}",
        )
        assert_bash_exec(
            bash,
            "_comp_cmd_ccc() {"
            "    local cur;"
            "    _comp_get_words cur;"
            "     unset -v COMPREPLY;"
            "    _comp_compgen_commands;"
            "}; complete -F _comp_cmd_ccc ccc",
        )

    def test_basic(self, bash, functions):
        output = assert_bash_exec(
            bash, "_comp_compgen_commands__test sh", want_output=True
        )
        assert output.strip()

    @pytest.mark.parametrize(
        "shopt_no_empty,result_empty", ((True, True), (False, False))
    )
    def test_empty(self, bash, functions, shopt_no_empty, result_empty):
        with bash_env_saved(bash) as bash_env:
            bash_env.shopt("no_empty_cmd_completion", shopt_no_empty)
            output = assert_bash_exec(
                bash, "_comp_compgen_commands__test", want_output=True
            )
        assert (output.strip() == "") == result_empty

    @pytest.mark.complete("ccc shared/default/bar")
    def test_spaces(self, functions, completion):
        assert completion == r"\ bar.d/"

    @pytest.mark.parametrize("direxpand", (False, True))
    @pytest.mark.parametrize("command", ("ccc", "exec", "nohup", "sudo"))
    @pytest.mark.parametrize(
        "directory,expected",
        [
            (".local", "al/"),
            (".local folder", r"al\ folder/"),
            (".local'quote", r"al\'quote/"),
            (".local:colon", r"al\:colon/"),
        ],
    )
    def test_tilde_directory(
        self,
        bash,
        functions,
        tmp_path,
        direxpand,
        command,
        directory,
        expected,
    ):
        (tmp_path / directory).mkdir()
        has_direxpand = bool(
            assert_bash_exec(
                bash, "shopt -p direxpand 2>/dev/null; :", want_output=None
            ).strip()
        )
        if direxpand and not has_direxpand:
            pytest.skip("direxpand is unavailable")
        with bash_env_saved(bash) as bash_env:
            bash_env.chdir(str(tmp_path))
            if has_direxpand:
                bash_env.shopt("direxpand", direxpand)
            assert assert_complete(bash, f"{command} ~+/.loc") == expected

    @pytest.mark.parametrize("direxpand", (False, True))
    def test_no_match_preserves_direxpand(
        self, bash, functions, tmp_path, direxpand
    ):
        if not assert_bash_exec(
            bash, "shopt -p direxpand 2>/dev/null; :", want_output=None
        ).strip():
            pytest.skip("direxpand is unavailable")
        with bash_env_saved(bash) as bash_env:
            bash_env.chdir(str(tmp_path))
            bash_env.shopt("direxpand", direxpand)
            assert assert_complete(bash, "ccc ~+/missing") == []

    @pytest.mark.parametrize("array", ("i", "REPLY", "result"))
    def test_tilde_directory_output_array(
        self, bash, functions, tmp_path, array
    ):
        if not assert_bash_exec(
            bash, "shopt -p direxpand 2>/dev/null; :", want_output=None
        ).strip():
            pytest.skip("direxpand is unavailable")
        (tmp_path / ".local").mkdir()
        assert_bash_exec(
            bash,
            "_comp_cmd_arrayccc() {"
            "    local cur; _comp_get_words cur;"
            f"    local -a {array}=();"
            f"    _comp_compgen -v {array} commands;"
            f'    COMPREPLY=("${{{array}[@]}}");'
            "}; complete -F _comp_cmd_arrayccc arrayccc",
        )
        with bash_env_saved(bash) as bash_env:
            bash_env.chdir(str(tmp_path))
            bash_env.shopt("direxpand", True)
            assert assert_complete(bash, "arrayccc ~+/.loc") == "al/"
