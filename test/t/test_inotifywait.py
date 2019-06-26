import pytest


class TestInotifywait:
    @pytest.mark.complete("inotifywait ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("inotifywait --", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("inotifywait -e ", require_cmd=True)
    def test_3(self, completion):
        assert completion
