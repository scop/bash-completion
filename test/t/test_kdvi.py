import shlex
from pathlib import Path
from typing import List, Tuple

import pytest

from conftest import assert_bash_exec, assert_complete, prepare_fixture_dir


class TestKdvi:
    @pytest.fixture(scope="class")
    def setup_fixture(
        self, request: pytest.FixtureRequest
    ) -> Tuple[Path, List[str], List[str]]:
        return prepare_fixture_dir(
            request,
            (
                ".dvi .DVI .dvi.bz2 .DVI.bz2 .dvi.gz .DVI.gz .dvi.Z .DVI.Z "
                ".txt"
            ).split(),
            "foo".split(),
        )

    def test_1(self, bash, setup_fixture):
        fixture_dir, files, dirs = setup_fixture

        assert_bash_exec(bash, "cd %s" % shlex.quote(str(fixture_dir)))
        try:
            completion = assert_complete(bash, "kdvi ")
        finally:
            assert_bash_exec(bash, "cd -", want_output=None)

        assert completion == [
            x
            for x in sorted(files + ["%s/" % d for d in dirs])
            if x.lower() != ".txt"
        ]
