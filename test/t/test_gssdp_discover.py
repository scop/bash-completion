import pytest


@pytest.mark.bashcomp(cmd="gssdp-discover")
class TestGssdpDiscover:
    @pytest.mark.complete("gssdp-discover ")
    def test_no_args(self, completion):
        assert not completion

    @pytest.mark.complete("gssdp-discover --", require_cmd=True)
    def test_options(self, completion):
        assert completion

    @pytest.mark.complete(
        "gssdp-discover --message-type=",
        skipif=(
            "! gssdp-discover --help 2>&1 "
            "| command grep -qF -- --message-type"
        ),
    )
    def test_message_type(self, completion):
        assert completion
