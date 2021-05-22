import pytest

from conftest import assert_complete, create_dummy_filedirs


@pytest.mark.bashcomp(temp_cwd=True)
class TestKpdf:
    def test_1(self, bash):
        files, dirs = create_dummy_filedirs(
            ".eps .EPS .pdf .PDF .ps .PS .txt".split(),
            "foo".split(),
        )

        completion = assert_complete(bash, "kpdf ")
        assert completion == [
            x
            for x in sorted(files + ["%s/" % d for d in dirs])
            if x.lower() != ".txt"
        ]
