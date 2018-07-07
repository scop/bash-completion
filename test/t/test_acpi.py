import pytest


class TestAcpi(object):

    @pytest.mark.complete("acpi -")
    def test_1(self, completion):
        assert completion.list
