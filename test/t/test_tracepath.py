import pytest


class TestTracepath:
    @pytest.mark.complete("tracepath ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("tracepath -", require_cmd=True)
    def test_2(self, completion):
        assert completion
