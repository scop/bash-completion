import os

import pytest


class TestIfup:

    @pytest.mark.xfail(bool(os.environ.get("CI")),
                       reason="Probably fails in CI")
    @pytest.mark.complete("ifup ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.xfail(bool(os.environ.get("CI")),
                       reason="Probably fails in CI")
    @pytest.mark.complete("ifup --")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.complete("ifup bash-completion ")
    def test_3(self, completion):
        assert not completion.list
