import pytest


class TestMunindoc:
    # Assume at least munin* available
    # require_cmd is not strictly correct here, but...
    @pytest.mark.complete("munindoc m", require_cmd=True)
    def test_1(self, completion):
        assert completion
