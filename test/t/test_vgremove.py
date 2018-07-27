import pytest


class TestVgremove:

    @pytest.mark.complete("vgremove -",
                          skipif="! vgremove --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
