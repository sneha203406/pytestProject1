class TestClass:
    def test_one(self):
        x = "sample"
        assert "l" in x
        print("test_1")

    def test_two(self):
        x = "hello"
        assert "o" in x
        print("test2")


t = TestClass()
t.test_one()
t.test_two()