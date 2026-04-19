import os

import pytest

from conftest import in_container


class TestIfup:
    @pytest.mark.skipif(
        os.environ.get("NETWORK") == "none",
        reason="There won't be any configured interfaces without network",
    )
    @pytest.mark.skipif(in_container(), reason="Probably fails in a container")
    @pytest.mark.complete("ifup ", require_cmd=True)
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
