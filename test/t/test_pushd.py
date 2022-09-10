import pytest


class TestPushd:
    @pytest.mark.complete("pushd ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("pushd -")
    def test_options(self, completion):
        assert completion
