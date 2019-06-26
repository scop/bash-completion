import pytest


class TestMock:
    @pytest.mark.complete("mock ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete(
        "mock -", require_cmd=True, xfail="! mock --help &>/dev/null"
    )
    def test_2(self, completion):
        assert completion
