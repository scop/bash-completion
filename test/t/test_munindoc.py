import pytest


class TestMunindoc:

    # Assume at least munin* available
    @pytest.mark.complete("munindoc m")
    def test_1(self, completion):
        assert completion
