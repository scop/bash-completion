import pytest


class TestCardctl(object):

    @pytest.mark.complete("cardctl ")
    def test_1(self, completion):
        assert completion.list
