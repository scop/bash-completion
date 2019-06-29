import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(ignore_env=r"^[+-]PORTSDIR=")
class TestPortinstall:
    @pytest.fixture(scope="class")
    def portsdir(self, request, bash):
        assert_bash_exec(bash, "PORTSDIR=$PWD/../tmp")
        assert_bash_exec(
            bash,
            "command sed -e s,PORTSDIR,$PORTSDIR,g "
            "pkgtools/ports/INDEX.dist >$PORTSDIR/INDEX",
        )
        assert_bash_exec(bash, "cp $PORTSDIR/INDEX $PORTSDIR/INDEX-5")
        request.addfinalizer(
            lambda: assert_bash_exec(bash, "rm $PORTSDIR/INDEX{,-5}")
        )

    @pytest.mark.complete("portinstall ", env=dict(PORTSDIR="$PWD/../tmp"))
    def test_1(self, completion, portsdir):
        assert (
            completion
            == "bash-2.05b.007_6 bash-3.1.17 bash-completion-20060301_2 "
            "shells/bash shells/bash-completion shells/bash2".split()
        )
