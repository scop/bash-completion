import pytest


class TestStream:
    @pytest.mark.complete("stream ")
    def test_1(self, completion):
        assert completion
