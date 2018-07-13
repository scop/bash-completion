import pytest


@pytest.mark.bashcomp(
    cmd="apt-cache",
)
class TestAptCache(object):

    @pytest.mark.complete("apt-cache ")
    def test_1(self, completion):
        assert completion.list
