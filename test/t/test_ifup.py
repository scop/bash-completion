import pytest

from conftest import in_container


class TestIfup:
    @pytest.mark.xfail(in_container(), reason="Probably fails in a container")
    @pytest.mark.complete("ifup ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete(
        "ifup -", require_cmd=True, skipif="! ifup --help &>/dev/null"
    )
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("ifup bash-completion ")
    def test_3(self, completion):
        assert not completion
