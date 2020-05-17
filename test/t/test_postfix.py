import getpass

import pytest


class TestPostfix:
    @pytest.mark.complete("postfix ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.xfail(
        getpass.getuser() != "root",
        reason="Likely outputs usage only for root",
    )
    @pytest.mark.complete(
        "postfix -",
        require_cmd=True,
        xfail="! type unbuffer &>/dev/null",
        sleep_after_tab=2,  # postfix is slow to output usage
    )
    def test_options(self, completion):
        assert completion
