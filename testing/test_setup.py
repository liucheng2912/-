# 模块
def setup_module():
    print("setup module")

def teardown_module():
    print("teardown ,module")


def test_case1():
    print("case1")

# 函数级 只对函数用例生效
def setup_function():
    print("setup function")

def teardown_function():
    print("teardown function")


class TestDemo:
    # 类前后分别执行
    def setup_class(self):
        print("setup class")

    def teardown_class(self):
        print("teardown class")
    # 每个方法的前和后
    def setup(self):
        print("setup method")

    def teardown(self):
        print("teardown method")

    def test_demo1(self):
        print("demo1")

    def test_demo2(self):
        print("demo1")

class TestDemo1:
    # 类前后分别执行
    def setup_class(self):
        print("setup class")

    def teardown_class(self):
        print("teardown class")
    # 每个方法的前和后
    def setup(self):
        print("setup method")

    def teardown(self):
        print("teardown method")

    def test_demo1(self):
        print("demo1")

    def test_demo2(self):
        print("demo1")