import pytest


class TestPwck:

    @pytest.mark.complete("pwck ")
    def test_1(self, completion):
        assert completion
