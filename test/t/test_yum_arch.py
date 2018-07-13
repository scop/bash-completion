import pytest


@pytest.mark.bashcomp(
    cmd="yum-arch",
)
class TestYumArch(object):

    @pytest.mark.complete("yum-arch -")
    def test_1(self, completion):
        assert completion.list
