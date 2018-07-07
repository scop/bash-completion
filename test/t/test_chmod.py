import pytest


class TestChmod(object):

    # No completion here until mode completion is implemented
    @pytest.mark.complete("chmod ")
    def test_1(self, completion):
        assert not completion.list

    @pytest.mark.complete("chmod 755 ")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.complete("chmod -")
    def test_3(self, completion):
        assert completion.list
