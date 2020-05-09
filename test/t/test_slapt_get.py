import os.path
from tempfile import mkstemp

import pytest

from conftest import assert_complete, is_bash_type


@pytest.mark.bashcomp(cmd="slapt-get")
class TestSlaptGet:
    @pytest.fixture(scope="class")
    def slapt_getrc(self, request, bash):
        fd, fname = mkstemp(prefix="slapt-getrc.", text=True)
        request.addfinalizer(lambda: os.remove(fname))
        with os.fdopen(fd, "w") as f:
            print(
                "WORKINGDIR=%s/"
                % os.path.join(bash.cwd, *"slackware var slapt-get".split()),
                file=f,
            )
            print("SOURCE=file:///home/", file=f)
        return fname

    @pytest.mark.complete("slapt-get -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("slapt-get --up", require_cmd=True)
    def test_2(self, completion):
        assert completion == "--update --upgrade".split()

    @pytest.mark.complete("slapt-get -c non-existent-file --install ")
    def test_3(self, completion):
        assert not completion

    def test_install(self, bash, slapt_getrc):
        if not is_bash_type(bash, "slapt-get"):
            pytest.skip("slapt-get not found")
        completion = assert_complete(
            bash, "slapt-get -c %s --install " % slapt_getrc
        )
        assert completion == sorted(
            "abc-4-i686-1 ran-1.2-noarch-1 qwe-2.1-i486-1".split()
        )
