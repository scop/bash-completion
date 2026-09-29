import pytest

from conftest import assert_complete, create_dummy_filedirs


@pytest.mark.bashcomp(temp_cwd=True)
class TestKdvi:
    def test_1(self, bash):
        files, dirs = create_dummy_filedirs(
            (
                ".dvi .DVI .dvi.bz2 .DVI.bz2 .dvi.gz .DVI.gz .dvi.Z .DVI.Z "
                ".txt"
            ).split(),
            "foo".split(),
        )

        completion = assert_complete(bash, "kdvi ")
        assert completion == [
            x
            for x in sorted(files + ["%s/" % d for d in dirs])
            if x.lower() != ".txt"
        ]
