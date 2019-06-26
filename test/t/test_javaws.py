import pytest


class TestJavaws:
    @pytest.mark.complete("javaws ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("javaws -", require_cmd=True)
    def test_2(self, completion):
        assert completion
