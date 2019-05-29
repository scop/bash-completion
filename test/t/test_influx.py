import pytest


class TestInflux:
    @pytest.mark.complete("influx ")
    def test_nothing(self, completion):
        assert not completion

    @pytest.mark.complete("influx -")
    def test_options(self, completion):
        assert completion

    @pytest.mark.complete("influx -format ")
    def test_format(self, completion):
        assert completion
