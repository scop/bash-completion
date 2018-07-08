import pytest


class TestDpkg(object):

    @pytest.mark.complete("dpkg --c")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("dpkg -L ")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.complete("dpkg -i ~")
    def test_3(self, completion):
        assert completion.list
