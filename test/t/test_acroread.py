import pytest


class TestAcroread:
    @pytest.mark.complete("acroread ", cwd="acroread")
    def test_1(self, completion):
        assert completion == "foo.d/ t.pdf".split()
