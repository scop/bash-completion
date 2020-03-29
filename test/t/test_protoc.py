import pytest


class TestProtoc:
    @pytest.mark.complete("protoc ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("protoc -", require_cmd=True)
    def test_2(self, completion):
        assert completion
        assert any(
            x.endswith("_out") or x.endswith("_out=") for x in completion
        )

    @pytest.mark.complete(
        "protoc --non_existent_plugin_out ", cwd="shared/default"
    )
    def test_all_out(self, completion):
        assert completion == ["bar bar.d/", "foo.d/"]
