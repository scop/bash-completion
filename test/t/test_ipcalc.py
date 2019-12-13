import pytest


class TestIpcalc:
    @pytest.mark.complete("ipcalc -", require_cmd=True)
    def test_options(self, completion):
        assert "--help" in completion

    @pytest.mark.complete("ipcalc --split -")
    def test_split_3args_1(self, completion):
        assert not completion

    @pytest.mark.complete("ipcalc --split 1 -")
    def test_split_3args_2(self, completion):
        assert not completion

    @pytest.mark.complete("ipcalc --split 1 2 -")
    def test_split_3args_3(self, completion):
        assert not completion

    @pytest.mark.complete("ipcalc --split 1 2 3 -", require_cmd=True)
    def test_split_3args_4(self, completion):
        assert "--help" in completion
