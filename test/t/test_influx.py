import pytest


class TestInflux:
    @pytest.mark.complete("influx ")
    def test_nothing(self, completion):
        assert not completion

    @pytest.mark.complete("influx -", require_cmd=True)
    def test_options(self, completion):
        assert completion

    @pytest.mark.complete("influx -format ", require_cmd=True)
    def test_format(self, completion):
        assert completion
