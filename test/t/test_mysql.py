import pytest


class Test(object):

    @pytest.mark.complete("mysql --")
    def test_dash(self, completion):
        assert completion.list

    @pytest.mark.complete("mysql --default-character-set=")
    def test_default_character_set(self, completion):
        assert completion.list
