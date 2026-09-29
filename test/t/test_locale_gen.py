import pytest


@pytest.mark.bashcomp(cmd="locale-gen")
class TestLocaleGen:
    # require_cmd is not strictly true here, but...
    @pytest.mark.complete("locale-gen ", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("locale-gen --", require_longopt=True)
    def test_2(self, completion):
        assert completion
