import pytest


class TestChage:

    @pytest.mark.complete("chage ")
    def test_1(self, completion):
        assert completion.list
