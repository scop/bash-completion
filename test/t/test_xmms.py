import pytest


class TestXmms:
    @pytest.mark.complete("xmms --", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("xmms --non-existent-option=--")
    def test_2(self, completion):
        assert not completion
