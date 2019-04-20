import pytest


class TestSvcadm:
    @pytest.mark.complete("svcadm ")
    def test_1(self, completion):
        assert completion
