import os

import pytest


class TestArp:

    @pytest.mark.complete("arp ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("arp -")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.xfail(bool(os.environ.get("CI")),
                       reason="Probably fails in CI")
    @pytest.mark.complete("arp -d ")
    def test_3(self, completion):
        assert completion.list
