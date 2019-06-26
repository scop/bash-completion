import pytest


@pytest.mark.bashcomp(cmd="deja-dup")
class TestDejaDup:
    @pytest.mark.complete("deja-dup -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("deja-dup --help ")
    def test_2(self, completion):
        assert not completion
