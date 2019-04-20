import pytest


class TestMock:
    @pytest.mark.complete("mock ")
    def test_1(self, completion):
        assert completion
