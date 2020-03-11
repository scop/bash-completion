import pytest


class TestPython3:
    @pytest.mark.complete("python3 ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("python3 -", require_cmd=True)
    def test_2(self, completion):
        assert len(completion) > 1

    @pytest.mark.complete("python3 -c ")
    def test_3(self, completion):
        assert not completion

    @pytest.mark.complete("python3 shared/default/")
    def test_4(self, completion):
        assert completion == ["bar bar.d/", "foo.d/"]

    @pytest.mark.complete("python3 -c foo shared/default/")
    def test_5(self, completion):
        assert completion == ["bar", "bar bar.d/", "foo", "foo.d/"]

    @pytest.mark.complete("python3 -c foo -")
    def test_6(self, completion):
        assert not completion

    @pytest.mark.complete("python3 -m foo -")
    def test_7(self, completion):
        assert not completion

    @pytest.mark.complete("python3 -m sy", require_cmd=True)
    def test_8(self, completion):
        assert completion

    @pytest.mark.complete("python3 -m json.", require_cmd=True)
    def test_9(self, completion):
        assert "json.tool" in completion
