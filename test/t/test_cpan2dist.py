import pytest


class TestCpan2dist(object):

    @pytest.mark.complete("cpan2dist -")
    def test_1(self, completion):
        assert completion.list
