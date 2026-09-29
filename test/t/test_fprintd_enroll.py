import pytest

from conftest import in_container


@pytest.mark.bashcomp(
    cmd="fprintd-enroll",
)
class TestFprintdEnroll:
    @pytest.mark.complete("fprintd-enroll ")
    def test_basic(self, completion):
        assert completion

    @pytest.mark.complete("fprintd-enroll -", require_cmd=True)
    def test_options(self, completion):
        assert completion

    @pytest.mark.skipif(
        in_container(), reason="Probably no fingerprint readers in container"
    )
    @pytest.mark.complete("fprintd-enroll --finger ", require_cmd=True)
    def test_finger(self, completion):
        assert completion
