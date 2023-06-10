import pytest


class TestDeclare:
    @pytest.mark.complete("declare -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("declare +", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("declare -p BASH_ARG")
    def test_3(self, completion):
        # bash 5.0 has BASH_ARGV0 too
        assert all(x in completion for x in "BASH_ARGC BASH_ARGV".split())

    @pytest.mark.complete("declare -f _comp_comp")
    def test_4(self, completion):
        assert "_comp_compgen" in completion

    @pytest.mark.complete("declare -a BASH_VERS")
    def test_arrayvar(self, completion):
        assert "INFO" in completion

    @pytest.mark.complete("declare -f BASH_VERS")
    def test_no_arrayvar_for_f(self, completion):
        assert "INFO" not in completion

    @pytest.mark.complete("declare -i BASH_VERS")
    def test_no_arrayvar_for_i(self, completion):
        assert "INFO" not in completion
