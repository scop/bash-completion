import pytest


@pytest.mark.pre_commands(
    "PATH=shared/bin:$PATH",
)
class TestWol(object):

    @pytest.mark.complete("wol ")
    def test_1(self, completion):
        assert completion.list == "00:00:00:00:00:00 11:11:11:11:11:11 " \
            "22:22:22:22:22:22 33:33:33:33:33:33".split()

    @pytest.mark.complete("wol 00:")
    def test_2(self, completion):
        assert completion.list == ["00:00:00:00:00:00"]
