import pytest


class TestProtoc:
    @pytest.mark.complete("protoc ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("protoc -")
    def test_2(self, completion):
        assert completion
