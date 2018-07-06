import pytest


class Test(object):

    @pytest.mark.complete("javac ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("javac -cp java/")
    def test_cp_fixture_dir(self, completion):
        assert completion.list == "a/ bashcomp.jar".split()
