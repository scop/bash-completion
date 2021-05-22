import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(ignore_env=r"^[+-]PORTSDIR=", temp_cwd=True)
class TestPortinstall:
    @pytest.fixture(scope="class")
    def portsdir(self, request, bash):
        assert_bash_exec(bash, "PORTSDIR=$PWD")
        assert_bash_exec(
            bash,
            "command sed -e s,PORTSDIR,$PORTSDIR,g "
            '"$SRCDIRABS"/fixtures/pkgtools/ports/INDEX.dist >INDEX',
        )
        assert_bash_exec(bash, "cp INDEX INDEX-5")

    @pytest.mark.complete("portinstall ", env=dict(PORTSDIR="$PWD"))
    def test_1(self, completion, portsdir):
        assert (
            completion
            == "bash-2.05b.007_6 bash-3.1.17 bash-completion-20060301_2 "
            "shells/bash shells/bash-completion shells/bash2".split()
        )
