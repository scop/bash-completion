import os

import pytest


class TestArp:

    @pytest.mark.xfail(bool(os.environ.get("CI")),
                       reason="Probably fails in CI")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("arp -")
    def test_2(self, completion):
        assert completion.list
