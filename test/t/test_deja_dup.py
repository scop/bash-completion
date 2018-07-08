import pytest


class TestDejaDup(object):

    @pytest.mark.complete("deja-dup -")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("deja-dup --help ")
    def test_2(self, completion):
        assert not completion.list
