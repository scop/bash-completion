import pytest


@pytest.mark.pre_commands(
    'export RI="-d ri"',
)
class Test(object):

    @pytest.mark.complete("ri -")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.xfail  # TODO: completion split issues (single space)
    @pytest.mark.complete("ri --dump=ri/")
    def test_dump(self, completion):
        assert completion.list == "BashCompletion/ cache.ri".split()

    @pytest.mark.complete("ri BashCompletio")
    def test_bashcompletion(self, completion):
        assert completion.list == ["BashCompletion"]
