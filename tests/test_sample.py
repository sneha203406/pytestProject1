class TestClass1:
    def test_one1(self):
        x = "sample"
        assert "l" in x
        print("test_one1")

    def test_two2(self):
        x = "hello"
        assert "e" in x
        print("test_two2")


t = TestClass1()


