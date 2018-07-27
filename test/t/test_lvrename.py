import pytest


class TestLvrename:

    @pytest.mark.complete("lvrename --",
                          skipif="! lvrename --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
