import pytest


class TestLvreduce:

    @pytest.mark.complete("lvreduce --",
                          skipif="! lvreduce --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
