import pytest


class TestUnexpand:

    @pytest.mark.complete("unexpand --",
                          skipif="! unexpand --help &>/dev/null")
    def test_1(self, completion):
        assert completion
