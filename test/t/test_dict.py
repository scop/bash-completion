import pytest


class TestDict:
    @pytest.mark.complete("dict -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("dict --database ", require_cmd=True)
    def test_database(self, completion):
        # Ensure the directory name "__load_completion/" not generated because
        # filenames in the current dictory (i.e., test/fixtures) are generated
        # by "-o default" when "_comp_cmd_dict" fails to generate any
        # completions.
        assert completion and "__load_completion/" not in completion
