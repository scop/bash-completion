import pytest


class TestAptBuild(object):

    @pytest.mark.complete("apt-build ")
    def test_1(self, completion):
        assert completion.list
