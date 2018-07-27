import pytest


class TestLvcreate:

    @pytest.mark.complete("lvcreate --",
                          skipif="! lvcreate --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
