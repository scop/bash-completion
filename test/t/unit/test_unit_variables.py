import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^[+-](___var|assoc[12])=")
class TestUnitVariables:
    @pytest.fixture(scope="class")
    def functions(self, request, bash):
        assert_bash_exec(bash, "unset assoc1 && declare -A assoc1=([idx]=1)")
        assert_bash_exec(
            bash, "unset assoc2 && declare -A assoc2=([idx1]=1 [idx2]=2)"
        )
        assert_bash_exec(bash, 'unset ${!___v*} && declare ___var=""')
        request.addfinalizer(
            lambda: assert_bash_exec(bash, "unset ___var assoc1 assoc2")
        )

    @pytest.mark.complete(": $___v")
    def test_simple_variable_name(self, functions, completion):
        assert completion == "ar"

    @pytest.mark.complete(": ${assoc1[")
    def test_single_array_index(self, functions, completion):
        assert completion == "idx]}"

    @pytest.mark.complete(": ${assoc2[")
    def test_multiple_array_indexes(self, functions, completion):
        assert completion == "${assoc2[idx1]} ${assoc2[idx2]}".split()

    @pytest.mark.complete(": ${assoc2[", shopt=dict(failglob=True))
    def test_multiple_array_indexes_failglob(self, functions, completion):
        assert completion == "${assoc2[idx1]} ${assoc2[idx2]}".split()

    @pytest.mark.complete(": ${assoc1[bogus]")
    def test_closing_curly_after_square(self, functions, completion):
        assert completion == "}"

    @pytest.mark.complete(": ${assoc1[@")
    def test_closing_brackets_after_at(self, functions, completion):
        assert completion == "]}"

    @pytest.mark.complete(": ${#___v")
    def test_hash_prefix(self, functions, completion):
        assert completion == "ar}"
