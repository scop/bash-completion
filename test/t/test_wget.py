import pytest


class TestWget:
    @pytest.mark.complete("wget ")
    def test_1(self, completion):
        assert not completion

    @pytest.mark.complete("wget --s", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("wget --bind-address=:")
    def test_3(self, completion):
        # Binding to ipv6 localhost
        assert ":1" in completion
