from itertools import chain

import pytest

from conftest import assert_bash_exec

LIVE_HOST = "bash_completion"


class TestScp:
    @pytest.mark.complete("scp -F config ", cwd="scp")
    def test_basic(self, hosts, completion):
        expected = sorted(
            chain(
                (
                    "%s:" % x
                    for x in chain(
                        hosts,
                        # From fixtures/scp/config
                        "gee hut".split(),
                        # From fixtures/scp/known_hosts
                        "blah doo ike".split(),
                    )
                ),
                # Local filenames
                ["config", "known_hosts", r"spaced\ \ conf"],
            )
        )
        assert completion == expected

    @pytest.mark.complete("scp -F 'spaced  conf' ", cwd="scp")
    def test_basic_spaced_conf(self, hosts, completion):
        expected = sorted(
            chain(
                (
                    "%s:" % x
                    for x in chain(
                        hosts,
                        # From "fixtures/scp/spaced  conf"
                        "gee jar".split(),
                        # From fixtures/scp/known_hosts
                        "blah doo ike".split(),
                    )
                ),
                # Local filenames
                ["config", "known_hosts", r"spaced\ \ conf"],
            )
        )
        assert completion == expected

    @pytest.mark.complete("scp -F")
    def test_capital_f_without_space(self, completion):
        assert completion
        assert not any(
            "option requires an argument -- F" in x for x in completion
        )

    @pytest.fixture(scope="class")
    def live_pwd(self, bash):
        try:
            return assert_bash_exec(
                bash,
                "ssh -o 'Batchmode yes' -o 'ConnectTimeout 1' "
                "%s pwd 2>/dev/null" % LIVE_HOST,
                want_output=True,
            ).strip()
        except AssertionError:
            pytest.skip("Live host %s not available" % LIVE_HOST)

    @pytest.mark.complete("scp %s:" % LIVE_HOST, sleep_after_tab=2)
    def test_live(self, live_pwd, completion):
        """
        To support this test, configure a HostName entry for LIVE_HOST
        in ssh's configs, e.g. ~/.ssh/config or /etc/ssh/ssh_config.

        Connection to it must open sufficiently quickly for the
        ConnectTimeout and sleep_after_tab settings.
        """
        assert completion == f"{LIVE_HOST}:{live_pwd}/"

    @pytest.mark.complete("scp -o Foo=")
    def test_option_arg(self, completion):
        assert not completion  # and no errors either

    @pytest.mark.complete(
        "scp hostname-not-expected-to-exist-in-known-hosts:",
        shopt=dict(nullglob=True),
    )
    def test_remote_path_with_nullglob(self, completion):
        assert not completion

    @pytest.mark.complete(
        "scp hostname-not-expected-to-exist-in-known-hosts:",
        shopt=dict(failglob=True),
    )
    def test_remote_path_with_failglob(self, completion):
        assert not completion
