# -*- encoding=utf8 -*-
from Base.BaseTestCase import BaseTestCase
from airtest.core.api import *
from Base.PublicFunction import *
from Base.BaseElement import *


class TestFeedback(BaseTestCase):

    def setUp(self):
        if self.poco(element('WelcomeActivity', 'Get_Start')).exists():  # get start 按钮
            self.poco(element('WelcomeActivity', 'Get_Start')).click()
            self.poco(element('MainActivity', 'Connect_Button')).wait(timeout=120)
            sleep()

    @frame("feedback", "feedback.html", "测试用户反馈")
    def test_feedback(self):
        self.poco(element('MainActivity', 'Menu')).click()
        sleep()
        self.poco(element('MainActivity', 'Help')).click()
        sleep()
        self.poco(element('HelpActivity', 'Feedback')).click()
        sleep()
        self.poco(element('HelpActivity', 'Submit')).click()
        sleep()
        is_view = self.poco(element('HelpActivity', 'Telegram')).exists()
        log('点击提交后', snapshot=True)
        assert_equal(False, is_view, '测试提交 feedback')
