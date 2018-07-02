import pytest


class Test(object):

    @pytest.mark.complete("acpi -")
    def test_dash(self, completion):
        assert completion.list
