import pytest

from 学习.pytest.pythoncode.calculator import Calculator


class TestCal:
    # def setup_class(self):
    #     # 实例变量
    #     self.cal = Calculator()
    #     print("计算开始")
    #
    # def teardown_class(self):
    #     # 实例变量
    #     print("计算结束")

    def setup(self):
        # 实例变量
        self.cal = Calculator()
        print("计算开始")

    def teardown(self):
        # 实例变量
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect',[
        [1,1,2],[100,100,200],[0.1,0.1,0.2],[-1,-1,-2],[1,0,1]
    ],ids=['int_case','big_case','fload_case','minus_case','zero_case'])
    def test_add(self,a,b,expect):
        # cal = Calculator()
        result = self.cal.add(a,b)
        assert result==expect
    #
    # def test_add1(self):
    #     # cal = Calculator()
    #     result = self.cal.add(100,100)
    #     assert result==200
    #
    # def test_add2(self):
    #     # cal = Calculator()
    #     result = self.cal.add(0.1,0.1)
    #     assert result==0.2
    @pytest.mark.parametrize('a,b,c',[
        [2,1,1],[100,1,99],[40,50,-10]
    ])
    def test_sub(self,a,b,c):
        # cal = Calculator()
        result = self.cal.sub(a, b)
        assert result == c
    @pytest.mark.parametrize('a,b,c',[
        [1,2,2],[0,1,0],[100,100,10000],[-1,-1,1]
    ])
    def test_mul(self,a,b,c):
        # cal = Calculator()
        result = self.cal.mul(a, b)
        assert result == c
    @pytest.mark.parametrize('a,b,c',[
        [2,1,2],[1,2,0.5],[0,1,0],[100,10,10],[-100,-4,25]
    ])
    def test_div(self,a,b,c):
        # cal = Calculator()
        result = self.cal.div1(a, b)
        assert result == c
