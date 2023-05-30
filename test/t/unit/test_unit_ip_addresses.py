import pytest

from conftest import assert_bash_exec, in_container


@pytest.mark.bashcomp(cmd=None, ignore_env=r"^\+COMPREPLY=")
class TestUnitIpAddresses:
    @pytest.fixture(scope="class")
    def functions(self, request, bash):
        assert_bash_exec(
            bash,
            "_ia() { local cur;_comp_get_words cur;"
            "unset -v COMPREPLY;_comp_compgen_ip_addresses; }",
        )
        assert_bash_exec(bash, "complete -F _ia ia")
        assert_bash_exec(
            bash,
            "_iaa() { local cur;_comp_get_words cur;"
            "unset -v COMPREPLY;_comp_compgen_ip_addresses -a; }",
        )
        assert_bash_exec(bash, "complete -F _iaa iaa")
        assert_bash_exec(
            bash,
            " _ia6() { local cur;_comp_get_words cur;"
            "unset -v COMPREPLY;_comp_compgen_ip_addresses -6; }",
        )
        assert_bash_exec(bash, "complete -F _ia6 ia6")

    def test_1(self, bash):
        assert_bash_exec(bash, "_comp_compgen_ip_addresses")

    @pytest.mark.complete("iaa ")
    def test_2(self, functions, completion):
        """_comp_compgen_ip_addresses -a should complete ip addresses."""
        assert completion
        assert all("." in x or ":" in x for x in completion)

    @pytest.mark.complete("ia ")
    def test_3(self, functions, completion):
        """_comp_compgen_ip_addresses should complete ipv4 addresses."""
        assert completion
        assert all("." in x for x in completion)

    @pytest.mark.xfail(in_container(), reason="Probably fails in a container")
    @pytest.mark.complete("ia6 ")
    def test_4(self, functions, completion):
        """_comp_compgen_ip_addresses -6 should complete ipv6 addresses."""
        assert completion
        assert all(":" in x for x in completion)
