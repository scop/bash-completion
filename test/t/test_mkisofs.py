import pytest


class TestMkisofs:
    @pytest.mark.complete("mkisofs ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("mkisofs -uid ")
    def test_2(self, completion):
        assert not [x for x in completion if not x.isdigit()]

    @pytest.mark.complete("mkisofs -gid ")
    def test_3(self, completion):
        assert not [x for x in completion if not x.isdigit()]
