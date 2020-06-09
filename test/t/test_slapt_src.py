import os
from tempfile import mkstemp

import pytest

from conftest import assert_complete, is_bash_type


@pytest.mark.bashcomp(cmd="slapt-src")
class TestSlaptSrc:
    @pytest.fixture(scope="class")
    def slapt_srcrc(self, request, bash):
        fd, fname = mkstemp(prefix="slapt-srcrc.", text=True)
        request.addfinalizer(lambda: os.remove(fname))
        with os.fdopen(fd, "w") as f:
            print(
                "BUILDDIR=%s/"
                % os.path.join(
                    bash.cwd, *"slackware usr src slapt-src".split()
                ),
                file=f,
            )
        return fname

    @pytest.mark.complete("slapt-src -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("slapt-src --bu", require_cmd=True)
    def test_2(self, completion):
        assert completion == "ild" or "--build" in completion

    @pytest.mark.complete("slapt-src --ins", require_cmd=True)
    def test_3(self, completion):
        assert completion == "tall" or "--install" in completion

    def test_install(self, bash, slapt_srcrc):
        if not is_bash_type(bash, "slapt-src"):
            pytest.skip("slapt-src not found")
        completion = assert_complete(
            bash, "slapt-src --config %s --install " % slapt_srcrc
        )
        assert completion == "abc:4 qwe:2.1".split()
