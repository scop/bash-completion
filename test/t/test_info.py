import pytest


@pytest.mark.bashcomp(pre_cmds=("INFOPATH+=:$PWD/info:",))
class TestInfo:
    @pytest.mark.complete("info bash")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("info -", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete(
        "info nonexistent-na",
        env=dict(INFOPATH="'$(echo malicious code >/dev/tty)'"),
    )
    def test_infopath_code_injection(self, completion):
        # no completion, no space appended
        assert not completion
