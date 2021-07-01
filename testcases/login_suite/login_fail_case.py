import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#驱动器目录
current = os.path.dirname(__file__)
chrome_driver_path = os.path.join(current,'../../webdriver/chromedriver.exe')

#打开浏览器
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.implicitly_wait(10)
driver.get('https://www.baidu.com/')

class LoginFailCase(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
        # time.sleep(3)
        # driver.quit()
    def test_fail_login(self):#错误登录
        driver.find_element(By.XPATH,'//a[@id="s-top-loginbtn"]').click()#点击登录
        #切换至用户名登录
        driver.find_element(By.XPATH,'//p[@data-type="normal"]').click()
        #输入用户名
        driver.find_element(By.XPATH,'//input[@id="TANGRAM__PSP_11__userName"]').send_keys('test1111')
        #输入密码
        driver.find_element(By.XPATH,'//input[@id="TANGRAM__PSP_11__password"]').send_keys('test2222')
        #点击登录
        driver.find_element(By.XPATH,'//input[@class="pass-button pass-button-submit"]').click()
        #设置断言,判断元素//span[@class="user-name c-font-normal c-color-t"] 是否存在
        self.assertTrue(EC.visibility_of((By.XPATH,'//span[@class="user-name c-font-normal c-color-t"]')))


if __name__ == '__main__':
    unittest.main()