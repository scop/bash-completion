import pytest


class Test(object):

    @pytest.mark.complete("pylint-3 --v")
    def test_v(self, completion):
        assert completion.list

    @pytest.mark.complete("pylint-3 http.clien")
    def test_python3_only_module(self, completion):
        assert completion.list
