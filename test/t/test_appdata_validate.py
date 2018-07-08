import pytest


class TestAppdataValidate(object):

    @pytest.mark.complete("appdata-validate ")
    def test_1(self, completion):
        assert completion.list
