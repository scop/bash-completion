import pytest


class TestFio:
    @pytest.mark.complete("fio ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("fio --", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("fio --debug=foo,", require_cmd=True)
    def test_3(self, completion):
        assert completion

    @pytest.mark.complete("fio --ioengin", require_cmd=True)
    def test_cmdhelp_all(self, completion):
        """Test we got a "known present" option from --cmdhelp=all."""
        assert completion == "e=" or "e" in completion

    @pytest.mark.complete("fio --ioengine=", require_cmd=True)
    def test_enghelp(self, completion):
        """Test --enghelp parsing."""
        assert completion
        assert all(x == x.strip() for x in completion)
        assert all(")" not in x for x in completion)

    @pytest.mark.complete("fio --unlink=", require_cmd=True)
    def test_cmdhelp_boolean(self, completion):
        """Test --cmdhelp=COMMAND boolean parsing."""
        assert completion == "0 1".split()

    @pytest.mark.complete("fio --kb_base=", require_cmd=True)
    def test_cmdhelp_valid_values(self, completion):
        """Test --cmdhelp=COMMAND valid values parsing."""
        # We expect kb_base args to be stable, no additions/removals.
        assert completion == "1000 1024".split()

    @pytest.mark.complete("fio --non_exist3nt_option=", require_cmd=True)
    def test_cmdhelp_nonexistent(self, completion):
        """Test --cmdhelp=COMMAND errors out gracefully."""
        assert not completion

    @pytest.mark.complete(
        "fio --crctest=",
        require_cmd=True,
        xfail="! fio --help 2>&1 | command grep -q -- --crctest",
    )
    def test_crctest(self, completion):
        assert "sha1" in completion

    @pytest.mark.complete("fio --debug=", require_cmd=True)
    def test_debug(self, completion):
        assert "process" in completion
