import pytest


class TestNproc:
    @pytest.mark.complete("nproc ")
    def test_1(self, completion):
        assert not completion

    @pytest.mark.complete("nproc --", require_longopt=True)
    def test_2(self, completion):
        assert completion
