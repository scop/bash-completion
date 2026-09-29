import pytest


class TestDoas:
    @pytest.mark.complete("doas -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("doas cd foo", cwd="shared/default")
    def test_2(self, completion):
        assert completion == ".d/"
        assert not completion.endswith(" ")

    @pytest.mark.complete("doas sh share")
    def test_3(self, completion):
        assert completion == "d/"
        assert not completion.endswith(" ")
