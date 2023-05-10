import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None)
class TestUtilCompgenSplit:
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
            "_comp__test_cmd1() { echo foo bar; echo baz; }",
        )
        assert_bash_exec(
            bash,
            '_comp__test_attack() { echo "\\$(echo should_not_run >&2)"; }',
        )

    def test_1_basic(self, bash, functions):
        output = assert_bash_exec(
            bash,
            '_comp__test_compgen split -- "$(_comp__test_cmd1)"',
            want_output=True,
        )
        assert output.strip() == "<foo><bar><baz>"

    def test_2_attack(self, bash, functions):
        output = assert_bash_exec(
            bash,
            '_comp__test_compgen split -- "$(_comp__test_attack)"',
            want_output=True,
        )
        assert output.strip() == "<$(echo><should_not_run><>&2)>"

    def test_3_sep1(self, bash, functions):
        output = assert_bash_exec(
            bash,
            '_comp__test_compgen split -l -- "$(_comp__test_cmd1)"',
            want_output=True,
        )
        assert output.strip() == "<foo bar><baz>"

    def test_3_sep2(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "_comp__test_compgen split -F $'b\\n' -- \"$(_comp__test_cmd1)\"",
            want_output=True,
        )
        assert output.strip() == "<foo ><ar><az>"

    def test_4_optionX(self, bash, functions):
        output = assert_bash_exec(
            bash,
            '_comp__test_compgen split -X bar -- "$(_comp__test_cmd1)"',
            want_output=True,
        )
        assert output.strip() == "<foo><baz>"

    def test_4_optionS(self, bash, functions):
        output = assert_bash_exec(
            bash,
            '_comp__test_compgen split -S .txt -- "$(_comp__test_cmd1)"',
            want_output=True,
        )
        assert output.strip() == "<foo.txt><bar.txt><baz.txt>"

    def test_4_optionP(self, bash, functions):
        output = assert_bash_exec(
            bash,
            '_comp__test_compgen split -P /tmp/ -- "$(_comp__test_cmd1)"',
            want_output=True,
        )
        assert output.strip() == "</tmp/foo></tmp/bar></tmp/baz>"

    def test_4_optionPS(self, bash, functions):
        output = assert_bash_exec(
            bash,
            '_comp__test_compgen split -P [ -S ] -- "$(_comp__test_cmd1)"',
            want_output=True,
        )
        assert output.strip() == "<[foo]><[bar]><[baz]>"

    def test_5_empty(self, bash, functions):
        output = assert_bash_exec(
            bash, '_comp__test_compgen split -- ""', want_output=True
        )
        assert output.strip() == ""

    def test_5_empty2(self, bash, functions):
        output = assert_bash_exec(
            bash, '_comp__test_compgen split -- " "', want_output=True
        )
        assert output.strip() == ""
