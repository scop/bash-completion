import os

import pytest

from conftest import assert_complete, is_bash_type


@pytest.mark.bashcomp(cmd="slapt-src")
class TestSlaptSrc:
    @pytest.fixture(scope="class")
    def slapt_srcrc(self, bash, tmp_path_factory):
        build_dir = os.path.join(
            bash.cwd, *"slackware usr src slapt-src".split()
        )

        tmpdir = tmp_path_factory.mktemp(
            "bash-completion._comp_cmd_slapt_src."
        )
        tmpfile = tmpdir / "slapt-srcrc.0"
        tmpfile.write_text(f"BUILDDIR={build_dir}/\n")
        return str(tmpfile)

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
