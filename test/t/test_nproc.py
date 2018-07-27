import pytest


class TestNproc:

    @pytest.mark.complete("nproc ")
    def test_1(self, completion):
        assert not completion.list

    @pytest.mark.complete("nproc -")
    def test_2(self, completion):
        assert completion.list
