import pytest


class TestChgrp(object):

    @pytest.mark.complete("chgrp ")
    def test_1(self, completion):
        assert completion.list
