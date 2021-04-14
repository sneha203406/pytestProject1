class TestClass:
    def test_one(self):
        x = "sample"
        assert "l" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "hello")
