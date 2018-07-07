import pytest


class TestMdadm(object):

    @pytest.mark.complete("mdadm ")
    def test_1(self, completion):
        assert completion.list
