import pytest


@pytest.mark.bashcomp(cmd="xvfb-run")
class TestXvfbRun:
    @pytest.mark.complete("xvfb-run ")
    def test_no_args(self, completion):
        assert any(x in completion for x in ("bash", "xvfb-run"))

    @pytest.mark.complete("xvfb-run -", require_cmd=True)
    def test_options(self, completion):
        assert completion
