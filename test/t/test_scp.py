from itertools import chain

import pytest


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
