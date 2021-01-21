from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_frame.test_homework.basepage import BasePage
from test_frame.test_homework.page_wh.search import Search


class MainPage(BasePage):

    def goto_search(self):
        self.find_and_click((MobileBy.ID, 'post_status'))
        locator = (MobileBy.ID, "iv_close")
        #添加显示等待，防止弹窗元素未加载出来
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))
        self.find((MobileBy.XPATH, '//*[@text="行情"]')).click()
        self.find_and_click((MobileBy.ID, 'action_search'))
        return Search(self.driver)