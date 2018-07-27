import pytest


class TestStrings:

    @pytest.mark.complete("strings ")
    def test_1(self, completion):
        assert completion.list
