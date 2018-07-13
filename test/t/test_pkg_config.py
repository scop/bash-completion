import pytest


@pytest.mark.bashcomp(
    cmd="pkg-config",
)
class TestPkgConfig(object):

    @pytest.mark.complete("pkg-config ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("pkg-config -")
    def test_2(self, completion):
        assert completion.list
