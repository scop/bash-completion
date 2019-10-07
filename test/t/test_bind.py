import pytest


class TestBind:
    @pytest.mark.complete("bind -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("bind -q kill-w")
    def test_2(self, completion):
        assert all(
            x in completion for x in "kill-whole-line kill-word".split()
        )

    @pytest.mark.complete("bind 'x:ab")
    def test_3(self, completion):
        assert "x:abort" in completion
