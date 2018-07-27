import pytest


class TestGroupadd:

    @pytest.mark.complete("groupadd ")
    def test_1(self, completion):
        assert not completion.list

    @pytest.mark.complete("groupadd -")
    def test_2(self, completion):
        assert completion.list
