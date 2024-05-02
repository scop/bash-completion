import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(cmd=None)
class TestUtilCompgenAvailableInterfaces:
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

    def test_1_trailing_colons(self, bash, functions):
        output = assert_bash_exec(
            bash,
            "_comp__test_compgen available_interfaces",
            want_output=True,
        )
        assert ":>" not in output.strip()
