import pytest


class TestScreen:
    @pytest.mark.complete("screen -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("screen -c shared/default/")
    def test_2(self, completion):
        assert completion == ["bar", "bar bar.d/", "foo", "foo.d/"]

    @pytest.mark.complete("screen cat ")
    def test_3(self, completion):
        assert completion

    # Assume at least vt100 and friends are there
    @pytest.mark.complete("screen -T vt")
    def test_4(self, completion):
        assert completion

    @pytest.mark.complete("screen -T foo ca")
    def test_5(self, completion):
        assert completion == "t" or "cat" in completion

    @pytest.mark.complete("screen //")
    def test_telnet(self, completion):
        assert completion == "telnet"

    @pytest.mark.complete("screen cat //")
    def test_not_telnet(self, completion):
        assert completion != "telnet"

    @pytest.mark.complete("screen //telnet ", env=dict(HOME="$PWD/shared"))
    def test_telnet_first_arg(self, completion):
        assert "bash-completion-canary-host.local" in completion

    @pytest.mark.complete("screen //telnet foo ", env=dict(HOME="$PWD/shared"))
    def test_telnet_other_args(self, completion):
        assert not completion

    @pytest.mark.complete("screen /dev/ttyUSB0 ")
    def test_serial_2nd_arg(self, completion):
        assert "19200" in completion

    @pytest.mark.complete("screen /dev/ttyUSB0 9600 ")
    def test_serial_3rdplus_arg(self, completion):
        assert not completion
