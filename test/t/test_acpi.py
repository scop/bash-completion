import pytest


class TestAcpi:
    @pytest.mark.complete("acpi -", require_cmd=True)
    def test_1(self, completion):
        assert completion
