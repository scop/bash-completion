import pytest


@pytest.mark.bashcomp(cmd="tsig-keygen")
class TestTsigKeygen:
    @pytest.mark.complete("tsig-keygen ")
    def test_basic(self, completion):
        assert not completion

    @pytest.mark.complete("tsig-keygen -", require_cmd=True)
    def test_options(self, completion):
        assert completion
