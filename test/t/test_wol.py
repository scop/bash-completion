import pytest


@pytest.mark.bashcomp(pre_cmds=("PATH=$PWD/shared/bin:$PATH",))
class TestWol:
    @pytest.mark.complete("wol ")
    def test_1(self, completion):
        assert (
            completion == "00:00:00:00:00:00 11:11:11:11:11:11 "
            "22:22:22:22:22:22 33:33:33:33:33:33".split()
        )

    @pytest.mark.complete("wol 00:")
    def test_2(self, completion):
        assert completion == "00:00:00:00:00:00"

    @pytest.mark.complete("wol -")
    def test_3(self, completion):
        assert completion
