import pytest


class TestPkgrm:
    # require_cmd is not strictly true here, but...
    @pytest.mark.complete("pkgrm ", require_cmd=True)
    def test_1(self, completion):
        assert completion
