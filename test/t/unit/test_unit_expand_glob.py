import pytest

from conftest import assert_bash_exec, bash_env_saved


@pytest.mark.bashcomp(
    cmd=None,
    cwd="_filedir",
    ignore_env=r"^\+declare -f (dump_array|__tester)$",
)
class TestExpandGlob:
    @pytest.fixture(scope="class")
    def functions(self, bash):
        assert_bash_exec(
            bash,
            "dump_array() { ((${#arr[@]})) && printf '<%s>' \"${arr[@]}\"; echo; }",
        )
        assert_bash_exec(
            bash,
            '__tester() { local LC_ALL= LC_COLLATE=C arr; _comp_expand_glob arr "$@";dump_array; }',
        )

    def test_match_all(self, bash, functions):
        output = assert_bash_exec(bash, "__tester '*'", want_output=True)
        assert output.strip() == "<a b><a$b><a&b><a'b><ab><aé><brackets><ext>"

    def test_match_pattern(self, bash, functions):
        output = assert_bash_exec(bash, "__tester 'a*'", want_output=True)
        assert output.strip() == "<a b><a$b><a&b><a'b><ab><aé>"

    def test_match_unmatched(self, bash, functions):
        output = assert_bash_exec(
            bash, "__tester 'unmatched-*'", want_output=True
        )
        assert output.strip() == ""

    def test_match_multiple_words(self, bash, functions):
        output = assert_bash_exec(bash, "__tester 'b* e*'", want_output=True)
        assert output.strip() == "<brackets><ext>"

    def test_match_brace_expansion(self, bash, functions):
        output = assert_bash_exec(
            bash, "__tester 'brac{ket,unmatched}*'", want_output=True
        )
        assert output.strip() == "<brackets>"

    def test_protect_from_noglob(self, bash, functions):
        with bash_env_saved(bash, functions) as bash_env:
            bash_env.set("noglob", True)
            output = assert_bash_exec(bash, "__tester 'a*'", want_output=True)
            assert output.strip() == "<a b><a$b><a&b><a'b><ab><aé>"

    def test_protect_from_failglob(self, bash, functions):
        with bash_env_saved(bash) as bash_env:
            bash_env.shopt("failglob", True)
            output = assert_bash_exec(
                bash, "__tester 'unmatched-*'", want_output=True
            )
            assert output.strip() == ""

    def test_protect_from_nullglob(self, bash, functions):
        with bash_env_saved(bash) as bash_env:
            bash_env.shopt("nullglob", False)
            output = assert_bash_exec(
                bash, "__tester 'unmatched-*'", want_output=True
            )
            assert output.strip() == ""

    def test_protect_from_dotglob(self, bash, functions):
        with bash_env_saved(bash) as bash_env:
            bash_env.shopt("dotglob", True)
            output = assert_bash_exec(
                bash, "__tester 'ext/foo/*'", want_output=True
            )
            assert output.strip() == ""

    def test_protect_from_GLOBIGNORE(self, bash, functions):
        with bash_env_saved(bash) as bash_env:
            # Note: dotglob is changed by GLOBIGNORE
            bash_env.save_shopt("dotglob")
            bash_env.write_variable("GLOBIGNORE", "*")
            output = assert_bash_exec(bash, "__tester 'a*'", want_output=True)
            assert output.strip() == "<a b><a$b><a&b><a'b><ab><aé>"
