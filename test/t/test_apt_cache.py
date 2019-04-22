import pytest


@pytest.mark.bashcomp(cmd="apt-cache")
class TestAptCache:
    @pytest.mark.complete("apt-cache ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("apt-cache showsrc [")
    def test_2(self, completion):
        # Doesn't actually fail on grep errors, but takes a long time.
        assert not completion
