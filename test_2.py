import pytest
import allure


@pytest.mark.Demo2
@allure.epic('李国彬')
@allure.feature('Demo2模块')
class TestDemo2:

    @allure.title('Demo2模块用例1')
    def test_three(self):
        print('test_three测试通过')
        assert True

    @allure.title('Demo2模块用例2')
    def test_four(self):
        print('test_four测试不通过')
        assert False
