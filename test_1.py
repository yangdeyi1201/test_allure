import pytest
import allure


@pytest.mark.Demo1
@allure.epic('杨德义')
@allure.feature('Demo1模块')
class TestDemo1:

    @allure.title('Demo1模块用例1')
    def test_one(self):
        print('test_one测试通过')
        assert True

    @allure.title('Demo1模块用例2')
    def test_two(self):
        print('test_two测试不通过')
        assert False
