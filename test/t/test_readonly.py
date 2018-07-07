import pytest


class TestReadonly(object):

    @pytest.mark.complete("readonly BASH_ARG")
    def test_1(self, completion):
        assert completion.list
