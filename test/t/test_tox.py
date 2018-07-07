import pytest


class TestTox(object):

    @pytest.mark.complete("tox -")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("tox -e ")
    def test_2(self, completion):
        assert completion.list == ["ALL"]

    @pytest.mark.complete("tox -e foo,")
    def test_3(self, completion):
        assert completion.list == ["foo,ALL"]
