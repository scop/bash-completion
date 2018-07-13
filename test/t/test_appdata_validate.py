import pytest


@pytest.mark.bashcomp(
    cmd="appdata-validate",
)
class TestAppdataValidate(object):

    @pytest.mark.complete("appdata-validate ")
    def test_1(self, completion):
        assert completion.list
