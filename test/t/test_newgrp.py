import pytest


class Test(object):

    @pytest.mark.complete("newgrp ")
    def test_(self, completion):
        assert completion.list
