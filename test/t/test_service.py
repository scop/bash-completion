import sys

import pytest

from conftest import assert_complete, bash_env_saved


class TestService:
    @pytest.mark.xfail(
        sys.platform == "darwin",
        reason="Service completion not available on macOS",
    )
    def test_1(self, bash):
        with bash_env_saved(bash) as bash_env:
            bash_env.write_variable(
                "_comp__test_inetd_dir",
                "%s/_comp_compgen_xinetd_services/xinetd.d" % bash.cwd,
            )
            completion = assert_complete(bash, "service ")
            assert all(x in completion for x in ("arp", "ifconfig"))
