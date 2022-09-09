import pytest


class TestFio:
    @pytest.mark.complete("fio ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("fio --", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("fio --debug=foo,")
    def test_3(self, completion):
        assert completion

    @pytest.mark.complete("fio --ioengin", require_cmd=True)
    def test_cmdhelp_all(self, completion):
        """Test we got a "known present" option from --cmdhelp=all."""
        assert completion == "e=" or "e" in completion
