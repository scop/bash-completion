from itertools import chain

import pytest


class TestSftp:
    @pytest.mark.complete("sftp -Fsp", cwd="sftp")
    def test_1(self, completion):
        assert completion == r"aced\ \ conf"

    @pytest.mark.complete("sftp -", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("sftp -F config ", cwd="sftp")
    def test_hosts(self, hosts, completion):
        expected = sorted(
            chain(
                hosts,
                # From fixtures/sftp/config
                "gee hut".split(),
                # From fixtures/sftp/known_hosts
                "10.10.10.10 doo ike".split(),
            )
        )
        assert completion == expected

    @pytest.mark.complete(r"sftp -F spaced\ \ conf ", cwd="sftp")
    def test_hosts_spaced_conf(self, hosts, completion):
        expected = sorted(
            chain(
                hosts,
                # From "fixtures/sftp/spaced  conf"
                "gee jar".split(),
                # From fixtures/sftp/known_hosts
                "10.10.10.10 doo ike".split(),
            )
        )
        assert completion == expected

    @pytest.mark.complete("sftp -F")
    def test_capital_f_without_space(self, completion):
        assert completion
        assert not any(
            "option requires an argument -- F" in x for x in completion
        )
