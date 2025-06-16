import pytest

from conftest import assert_bash_exec, bash_env_saved


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

    # We fallback to ifconfig if ip fails, so we want to check also the scenario without ip.
    @pytest.fixture(scope="function", params=["ip", "ifconfig"])
    def remove_one_tool(self, request, bash):
        assert_bash_exec(bash, f"{request.param}() {{ false; }}")
        yield
        assert_bash_exec(bash, f"unset -f {request.param}")

    def test_1_trailing_colons(self, bash, functions, remove_one_tool):
        output = assert_bash_exec(
            bash,
            "_comp__test_compgen available_interfaces",
            want_output=True,
        )
        assert ":>" not in output.strip()

    def test_2_correct_interfaces(self, bash, functions, remove_one_tool):
        with bash_env_saved(bash) as bash_env:
            # Using emulated ip and ifconfig commands
            bash_env.write_variable(
                "PATH", "$PWD/shared/bin:$PATH", quote=False
            )
            output = assert_bash_exec(
                bash,
                "_comp__test_compgen available_interfaces",
                want_output=True,
            )
            assert all(
                iface in output
                for iface in ["<eth0>", "<lo>", "<peer1>", "<peer2>"]
            )
