import pytest


class TestMcrypt:
    @pytest.mark.complete("mcrypt ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("mcrypt -a ", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("mcrypt -m ", require_cmd=True)
    def test_3(self, completion):
        assert completion

    @pytest.mark.complete("mcrypt -", require_cmd=True)
    def test_4(self, completion):
        assert completion
