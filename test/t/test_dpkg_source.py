import pytest


@pytest.mark.bashcomp(
    cmd="dpkg-source",
)
class TestDpkgSource(object):

    @pytest.mark.complete("dpkg-source -")
    def test_1(self, completion):
        assert completion.list
