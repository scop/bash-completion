import pytest


class TestMknod(object):

    @pytest.mark.complete("mknod ")
    def test_1(self, completion):
        assert completion.list
