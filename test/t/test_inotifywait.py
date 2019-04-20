import pytest


class TestInotifywait:
    @pytest.mark.complete("inotifywait ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("inotifywait --")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("inotifywait -e ")
    def test_3(self, completion):
        assert completion
