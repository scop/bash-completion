import pytest


@pytest.mark.bashcomp(ignore_env=r"^\+_tshark_protocols=")
class TestTshark:

    @pytest.mark.complete("tshark -")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("tshark -G ")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.complete("tshark -O foo,htt")
    def test_3(self, completion):
        assert "http" in completion.list
