import pytest


class TestFirefox:

    @pytest.mark.complete("firefox ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("firefox -")
    def test_2(self, completion):
        assert completion.list
        assert not completion.line.endswith(" ")
