import pytest


class TestApache2ctl:
    @pytest.mark.complete("apache2ctl ")
    def test_1(self, completion):
        assert completion
