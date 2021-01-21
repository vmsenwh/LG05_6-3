from appium.webdriver.common.mobileby import MobileBy
from test_frame.test_homework.basepage import BasePage


class Search(BasePage):

    def get_text(self):
        result = self.find((MobileBy.XPATH, '//*[@text="今日热点"]')).text
        return result