from test_frame.test_homework.app import App


class TestSearch:

    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    def test_search(self):
        result = self.main.goto_search().get_text()
        assert result == "今日热点"