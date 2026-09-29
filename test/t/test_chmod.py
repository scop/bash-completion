import pytest


class TestChmod:
    # No completion here until mode completion is implemented
    @pytest.mark.complete("chmod ")
    def test_1(self, completion):
        assert not completion

    @pytest.mark.complete("chmod 755 ")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("chmod -", require_cmd=True)
    def test_3(self, completion):
        assert completion

    @pytest.mark.complete("chmod -x ")
    def test_4(self, completion):
        assert completion

    @pytest.mark.complete("chmod -77 ")
    def test_5(self, completion):
        assert completion
