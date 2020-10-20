import allure
import pytest

"""
BLOCKER = 'blocker'　　  # 阻塞缺陷
CRITICAL = 'critical'　  # 严重缺陷
NORMAL = 'normal'　　    # 一般缺陷
MINOR = 'minor'　　      # 次要缺陷
TRIVIAL = 'trivial'　　  # 轻微缺陷
"""


# feature() 给功能模块取个名字 一个功能模块包含多个功能点 一般一个功能模块就作为一个类

@allure.feature('购物车功能')
class TestShoppingTrolley:
    # 定义用例级别
    severitis = ['blocker', 'critical', 'normal', 'minor', 'trivial']

    # story() 给功能点取个名字 一般一个功能点就作为一个方法
    @allure.severity(severitis[1])
    @allure.story('加入购物车')
    def test_add_shopping_trolley(self):
        # 步骤1  因为login() 被装饰器 @allure.step()装饰过 报告中会将步骤详细展示出来
        login('刘春明', '密码')
        # 步骤2
        with allure.step("浏览商品"):
            # attach() 添加文本信息到报告中
            allure.attach('笔记本', '商品1')
            allure.attach('手机', '商品2')
            # attach() 添加截图信息到报告中
            with open('./商品3截图.png', 'rb') as f:
                file = f.read()
            allure.attach(file, '商品3', allure.attachment_type.PNG)
        # 步骤3
        with allure.step("点击商品"):
            pass
        # 步骤4
        with allure.step("校验结果"):
            allure.attach('添加购物车成功', '期望结果')
            allure.attach('添加购物车失败', '实际结果')
            assert 'success' == 'failed'

    @allure.severity(severitis[0])
    @allure.story('修改购物车')
    def test_edit_shopping_trolley(self):
        pass

    @allure.severity(severitis[2])
    @pytest.mark.skipif(reason='本次不执行')
    @allure.story('删除购物车中商品')
    def test_delete_shopping_trolley(self):
        pass


@allure.step('用户登录')
def login(user, pwd):
    print(user, pwd)
