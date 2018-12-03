import os

import pytest


class TestIfdown:

    @pytest.mark.xfail(bool(os.environ.get("CI")),
                       reason="Probably fails in CI")
    @pytest.mark.complete("ifdown ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("ifdown bash-completion ")
    def test_2(self, completion):
        assert not completion.list
