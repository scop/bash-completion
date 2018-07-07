import pytest


class TestRdesktop(object):

    @pytest.mark.complete("rdesktop -")
    def test_1(self, completion):
        assert completion.list
