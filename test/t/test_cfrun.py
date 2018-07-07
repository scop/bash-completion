import pytest


class TestCfrun(object):

    @pytest.mark.complete("cfrun -")
    def test_1(self, completion):
        assert completion.list
