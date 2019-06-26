import pytest


@pytest.mark.bashcomp(cmd="appdata-validate")
class TestAppdataValidate:
    @pytest.mark.complete("appdata-validate ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("appdata-validate -", require_cmd=True)
    def test_2(self, completion):
        assert completion
