import pytest


class TestGpgv(object):

    @pytest.mark.complete("gpgv ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("gpgv -")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.complete("gpgv foo.sig foo ")
    def test_3(self, completion):
        assert not completion.list
