import os

import pytest


class TestDict:
    @pytest.mark.complete("dict -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.xfail(
        os.environ.get("NETWORK") == "none",
        reason="The database list is unavailable without network",
    )
    @pytest.mark.complete("dict --database ", require_cmd=True)
    def test_database(self, completion):
        # Ensure the directory name "_comp_load/" not generated because
        # filenames in the current dictory (i.e., test/fixtures) are generated
        # by "-o default" when "_comp_cmd_dict" fails to generate any
        # completions.
        assert completion and "_comp_load/" not in completion

    @pytest.mark.xfail(
        os.environ.get("NETWORK") == "none",
        reason="The database list is unavailable without network",
    )
    @pytest.mark.complete(
        "dict -h dict.org --database ", require_cmd=True, env=dict(IFS="")
    )
    def test_database_IFS(self, completion):
        assert completion and "_comp_load/" not in completion
