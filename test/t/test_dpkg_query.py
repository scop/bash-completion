import os.path

import pytest


@pytest.mark.bashcomp(cmd="dpkg-query")
class TestDpkgQuery:
    @pytest.mark.complete("dpkg-query --", require_cmd=True)
    def test_options(self, completion):
        assert completion

    @pytest.mark.xfail(
        not os.path.exists("/etc/debian_version"),
        reason="Likely fails on systems not based on Debian",
    )
    @pytest.mark.complete(
        "dpkg-query -W dpk",
        require_cmd=True,
        xfail="! apt-cache show &>/dev/null",  # empty cache?
    )
    def test_show(self, completion):
        assert "dpkg" in completion
