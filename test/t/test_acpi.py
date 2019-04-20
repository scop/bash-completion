import pytest


class TestAcpi:
    @pytest.mark.complete("acpi -")
    def test_1(self, completion):
        assert completion
