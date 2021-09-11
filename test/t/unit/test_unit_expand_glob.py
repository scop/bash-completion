import pytest

from conftest import assert_bash_exec, bash_env_saved


@pytest.mark.bashcomp(
    cmd=None,
    cwd="_filedir",
    ignore_env=r"^\+(my_array=|declare -f dump_array$)",
)
class TestExpandGlob:
    def test_match_all(self, bash):
        assert_bash_exec(
            bash,
            "dump_array() { ((${#my_array[@]})) && printf '<%s>' \"${my_array[@]}\"; echo; }",
        )
        output = assert_bash_exec(
            bash,
            "LC_ALL= LC_COLLATE=C _comp_expand_glob my_array '*';dump_array",
            want_output=True,
        )
        assert output.strip() == "<a b><a$b><a&b><a'b><ab><aé><brackets><ext>"

    def test_match_pattern(self, bash):
        output = assert_bash_exec(
            bash,
            "LC_ALL= LC_COLLATE=C _comp_expand_glob my_array 'a*';dump_array",
            want_output=True,
        )
        assert output.strip() == "<a b><a$b><a&b><a'b><ab><aé>"

    def test_match_unmatched(self, bash):
        output = assert_bash_exec(
            bash,
            "_comp_expand_glob my_array 'unmatched-*';dump_array",
            want_output=True,
        )
        assert output.strip() == ""

    def test_match_multiple_words(self, bash):
        output = assert_bash_exec(
            bash,
            "_comp_expand_glob my_array 'b* e*';dump_array",
            want_output=True,
        )
        assert output.strip() == "<brackets><ext>"

    def test_match_brace_expansion(self, bash):
        output = assert_bash_exec(
            bash,
            "_comp_expand_glob my_array 'brac{ket,unmatched}*';dump_array",
            want_output=True,
        )
        assert output.strip() == "<brackets>"

    def test_protect_from_noglob(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.set("noglob", True)
            output = assert_bash_exec(
                bash,
                "LC_ALL= LC_COLLATE=C _comp_expand_glob my_array 'a*';dump_array",
                want_output=True,
            )
            assert output.strip() == "<a b><a$b><a&b><a'b><ab><aé>"

    def test_protect_from_failglob(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.shopt("failglob", True)
            output = assert_bash_exec(
                bash,
                "_comp_expand_glob my_array 'unmatched-*';dump_array",
                want_output=True,
            )
            assert output.strip() == ""

    def test_protect_from_nullglob(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.shopt("nullglob", False)
            output = assert_bash_exec(
                bash,
                "_comp_expand_glob my_array 'unmatched-*';dump_array",
                want_output=True,
            )
            assert output.strip() == ""

    def test_protect_from_dotglob(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.shopt("dotglob", True)
            output = assert_bash_exec(
                bash,
                "_comp_expand_glob my_array 'ext/foo/*';dump_array",
                want_output=True,
            )
            assert output.strip() == ""

    def test_protect_from_GLOBIGNORE(self, bash):
        with bash_env_saved(bash) as bash_env:
            # Note: dotglob is changed by GLOBIGNORE
            bash_env.save_shopt("dotglob")
            bash_env.write_variable("GLOBIGNORE", "*")
            output = assert_bash_exec(
                bash,
                "LC_ALL= LC_COLLATE=C _comp_expand_glob my_array 'a*';dump_array",
                want_output=True,
            )
            assert output.strip() == "<a b><a$b><a&b><a'b><ab><aé>"
