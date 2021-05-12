class TestClass1:
    def test_one1(self):
        x = "sample"
        assert "l" in x
        print("success")

    def test_two2(self):
        x = "hello"
        assert "n" in x
        print("failure")


t = TestClass1()


