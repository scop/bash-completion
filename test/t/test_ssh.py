import pytest

from conftest import assert_complete, partialize


class TestSsh:
    @pytest.mark.complete("ssh -Fsp", cwd="ssh")
    def test_1(self, completion):
        assert completion == r"aced\ \ conf"

    @pytest.mark.complete("ssh -F config ls", cwd="ssh")
    def test_2(self, completion):
        """Should complete both commands and hostname."""
        assert all(x in completion for x in "ls ls_known_host".split())

    @pytest.mark.complete("ssh bash", cwd="ssh")
    def test_3(self, completion):
        """
        First arg should not complete with commands.

        Assumes there's no "bash" known host.
        """
        assert "bash" not in completion

    @pytest.mark.complete("ssh -vo AddressFamily=")
    def test_4(self, completion):
        assert completion

    @pytest.mark.xfail  # TODO our test facilities don't support case change?
    @pytest.mark.complete("ssh -vo userknownhostsf")
    def test_5(self, completion):
        assert "UserKnownHostsFile=" in completion

    @pytest.mark.complete("ssh -", require_cmd=True)
    def test_6(self, completion):
        assert completion

    @pytest.mark.complete("ssh -F")
    def test_capital_f_without_space(self, completion):
        assert completion
        assert not any(
            "option requires an argument -- F" in x for x in completion
        )

    @pytest.mark.complete("ssh -F nonexistent ")
    def test_capital_f_nonexistent(self, completion):
        assert completion

    def test_partial_hostname(self, bash, known_hosts):
        first_char, partial_hosts = partialize(bash, known_hosts)
        completion = assert_complete(bash, "ssh %s" % first_char)
        if len(completion) == 1:
            assert completion == partial_hosts[0][1:]
        else:
            assert completion == sorted(x for x in partial_hosts)

    @pytest.mark.parametrize("protocol", "4 6 9".split())
    def test_protocol_option_bundling(self, bash, protocol):
        completion = assert_complete(bash, "ssh -%sF ssh/" % protocol)
        assert "config" in completion
