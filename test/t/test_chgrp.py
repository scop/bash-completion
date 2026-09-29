import pytest


class TestChgrp:
    @pytest.mark.complete("chgrp ")
    def test_1(self, completion):
        assert completion
