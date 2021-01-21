from appium import webdriver

from test_frame.test_homework.page_wh.mainpage import MainPage
from test_frame.test_homework.basepage import BasePage


class App(BasePage):

    def start(self):
        if self.driver is None:
            desired_caps = {}
            desired_caps['platformName'] = "Android"
            desired_caps['deviceName'] = "127.0.0.1:7555"
            desired_caps['appPackage'] = "com.xueqiu.android"
            desired_caps['appActivity'] = ".view.WelcomeActivityAlias"
            desired_caps['noReset'] = "true"
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(10)
        return self

    def restart(self):
        self.driver.quit()
        self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()
        return self

    def goto_main(self) -> MainPage:
        return MainPage(self.driver)