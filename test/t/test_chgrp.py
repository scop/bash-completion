import pytest


class Test(object):

    @pytest.mark.complete("chgrp ")
    def test_(self, completion):
        assert completion.list
