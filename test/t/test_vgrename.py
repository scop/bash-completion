import pytest


class TestVgrename:

    @pytest.mark.complete("vgrename -",
                          skipif="! vgrename --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
