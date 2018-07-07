import pytest


class TestUseradd(object):

    @pytest.mark.complete("useradd ")
    def test_1(self, completion):
        assert not completion.list

    @pytest.mark.complete("useradd -")
    def test_2(self, completion):
        assert completion.list
