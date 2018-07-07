import pytest


class TestCiptool(object):

    @pytest.mark.complete("ciptool ")
    def test_1(self, completion):
        assert completion.list
