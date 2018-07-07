import pytest


class TestConfigList(object):

    @pytest.mark.complete("config_list -")
    def test_1(self, completion):
        assert completion.list
