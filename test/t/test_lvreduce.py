import pytest


class TestLvreduce:
    @pytest.mark.complete("lvreduce --", xfail="! lvreduce --help &>/dev/null")
    def test_1(self, completion):
        assert completion
