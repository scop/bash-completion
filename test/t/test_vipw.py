import sys

import pytest


class TestVipw:
    @pytest.mark.complete("vipw -", require_cmd=True)
    def test_1(self, completion):
        if sys.platform == "darwin":
            assert not completion  # takes no options
        else:
            assert completion
