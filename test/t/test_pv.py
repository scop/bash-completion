import pytest


class TestPv:
    @pytest.mark.complete("pv ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("pv -", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("pv --pidfile ")
    def test_3(self, completion):
        assert completion
