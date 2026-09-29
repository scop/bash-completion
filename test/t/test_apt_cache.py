import pytest


@pytest.mark.bashcomp(cmd="apt-cache")
class TestAptCache:
    @pytest.mark.complete("apt-cache ")
    def test_1(self, completion):
        assert "search" in completion

    @pytest.mark.complete("apt-cache showsrc [", require_cmd=True)
    def test_2(self, completion):
        # Doesn't actually fail on grep errors, but takes a long time.
        assert not completion

    @pytest.mark.complete("apt-cache ", trail=" add foo")
    def test_special_at_point(self, completion):
        assert not completion
