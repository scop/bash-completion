import pytest


class TestService(object):

    @pytest.mark.complete("service ")
    def test_1(self, completion):
        assert completion.list
