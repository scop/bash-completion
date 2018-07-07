import pytest


class TestCheckDb(object):

    @pytest.mark.complete("check_db -")
    def test_1(self, completion):
        assert completion.list
