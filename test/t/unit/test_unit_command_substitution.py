import pytest

from conftest import assert_bash_exec, assert_complete


@pytest.mark.bashcomp(
    cmd=None,
    ignore_env=r"^[+-](COMPREPLY|REPLY)=",
)
class TestUnitCommandSubstitution:
    """Test completion inside $() command substitutions."""

    wordlist = ["alpha", "bravo"]

    @pytest.fixture(scope="class")
    def functions(self, bash):
        assert_bash_exec(
            bash,
            # csub_cmd: a test command whose completion function returns
            # a fixed word list, filtered by the current word prefix.
            "_csub_compfunc() {"
            '  COMPREPLY=($(compgen -W "%s"'
            ' -- "${COMP_WORDS[COMP_CWORD]}"));'
            "}; "
            "complete -F _csub_compfunc csub_cmd" % " ".join(self.wordlist),
        )

    def test_closed_substitution(self, bash, functions):
        assert assert_complete(
            bash, "echo $(echo hi) ", cwd="shared/default"
        ) == ["bar", "bar bar.d/", "foo", "foo.d/"]

    def test_single_level(self, bash, functions):
        assert assert_complete(bash, "echo $(csub_cmd ") == self.wordlist

    def test_single_level_partial(self, bash, functions):
        assert assert_complete(bash, "echo $(csub_cmd a") == ["lpha"]

    def test_nested(self, bash, functions):
        assert (
            assert_complete(bash, "echo $(echo foo $(csub_cmd ")
            == self.wordlist
        )

    def test_nested_partial(self, bash, functions):
        assert assert_complete(bash, "echo $(echo foo $(csub_cmd b") == [
            "ravo"
        ]

    def test_closed_then_open(self, bash, functions):
        assert (
            assert_complete(bash, "echo $(echo hi) $(csub_cmd ")
            == self.wordlist
        )

    def test_open_then_closed(self, bash, functions):
        assert (
            assert_complete(bash, "echo $(csub_cmd $(echo hi) ")
            == self.wordlist
        )
