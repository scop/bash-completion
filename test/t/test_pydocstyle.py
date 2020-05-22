import pytest


class TestPydocstyle:
    @pytest.mark.complete("pydocstyle ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete(
        "pydocstyle -", require_cmd=True, require_longopt=True
    )
    def test_2(self, completion):
        assert completion
