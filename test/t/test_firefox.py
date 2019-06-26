import pytest


class TestFirefox:
    @pytest.mark.complete("firefox ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("firefox -", require_cmd=True)
    def test_2(self, completion):
        assert completion
        assert not completion.endswith(" ")
