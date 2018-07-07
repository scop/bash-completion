import pytest


class TestInterdiff(object):

    @pytest.mark.complete("interdiff ")
    def test_1(self, completion):
        assert completion.list
