class TestClass:
    def test_one(self):
        x = "sample"
        if (assert "l" in x):
            print("value found in x")
        else:
            print("value not found in x")
    def test_two(self):
        x = "hello"
        assert hasattr(x, "hello")