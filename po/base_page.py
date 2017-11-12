#!/usr/bin/python3
# coding:utf-8
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from common.log import Log
import time
import os
from config import global_parameters


class BasePage(object):

    log = Log()

    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    def wait(self, seconds):
        """
        隐示等待几秒
        :param seconds:                 几秒，int类型的数据
        :return:
        """
        self.driver.implicitly_wait(seconds)
        self.log.info("recessive waiting： %s 秒" % seconds)

    def quit(self):
        """
        退出程序
        :return:
        """
        self.driver.quit()
        self.log.info("退出程序")

    def key_code(self, num):
        """
        物理键盘操作
        :param num:                 所需操作的物理几盘号
        :return:
        """
        self.driver.press_keycode(num)
        self.log.info("keyboard： %s" % num)

    def switch_frame(self, loc):
        """
        切进iframe内嵌层
        :param loc:                 iframe定位器
        :return:                    切进iframe中
        """
        self.log.info(u"切换 iframe：%s" % loc)
        return self.driver.switch_to_frame(loc)

    def switch_webview(self):
        """
        从原生切到webview
        :return:                    切到webview
        """
        contexts = self.driver.contexts
        self.log.info("%s" % contexts)
        self.driver.switch_to.context(contexts[1])
        now = self.driver.current_context
        self.log.info("%s" % now)
        self.log.info("切换webview")

    def switch_native(self):
        """
        从webview切回原生
        :return:                    切到原生
        """
        self.driver.switch_to.context("NATIVE_APP")
        now = self.driver.current_context
        self.log.info("%s" % now)
        self.log.info(u"切回native")

    def find_element(self, *loc):
        """
        定位方法封装
        :param loc:                  定位器
        :return:                    定位元素
        """
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except Exception:
            self.log.info('Please enter the correct targeting elements')

    def get_text(self, *loc):
        """
        获取元素文本值
        :param loc:                 定位器
        :return:                    元素文本值
        """
        start_time = time.time()
        text = self.find_element(*loc).text
        self.log.info(u"Get the window title \t<%s -> %s>\t spend :%s time " % (loc[0], loc[1], time.time() - start_time))
        return text

    def click(self, *loc):
        """
        点击方法封装
        :param loc:                  定位器
        :return:
        """
        start_time = time.time()
        self.log.info(u"Click the element\t<%s -> %s>\t spend :%s time " % (loc[0], loc[1], time.time() - start_time))
        return self.find_element(*loc).click()

    def send_keys(self, value, *loc, clear_first=True):
        """
        输入方法封装
        :param clear_first:                 清理输入框中的内容
        :param loc:                         定位器
        :param value:                       输入的内容
        :return:
        """
        start_time = time.time()
        if clear_first:
            self.find_element(*loc).clear()
        self.log.info(u"Clear and input text to the element \t<%s -> %s>\t content: %s  spend :%s time " % (loc[0], loc[1], value, time.time() -start_time))
        return self.find_element(*loc).send_keys(value)

    @staticmethod
    def sleep(second):
        """
        强制等待多少秒
        :param second:                 几秒，int类型
        :return:                       强制等待多少秒
        """
        return time.sleep(second)

    def get_size(self):
        """
        获取屏幕大小
        :return:                       屏幕宽度高度
        """
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.log.info("获取手机屏幕大小：%s %s" % (x, y))
        return (x, y)

    def slide(self):
        """
        手机屏幕向下滑动
        :return:
        """
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.25)
        y2 = int(l[1] * 0.05)
        self.driver.swipe(x1, y1, x1, y2)
        self.log.info("向下滑动")

    @staticmethod
    def save_image(name):
        """
        截图保存路径
        :param name:                       图片名称 string类型
        :return:                           图片路径
        """
        day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        image_path = global_parameters.image_path + "\\" + day
        if not os.path.isdir(image_path):
            os.makedirs(image_path)
        image_name = os.path.join(image_path, '{0}_{1}.png'.format(time.strftime('%Y-%m-%d-%H_%M_%S'), name))
        print(image_name)
        return image_name

    def save_screenshot(self, name):
        """
        截图方法
        :param name:                       图片名称
        :return:
        """
        start_time = time.time()
        image = self.driver.save_screenshot(self.save_image(name))
        self.log.info("Screenshot of success：%s spend :%s time " % (name, time.time()-start_time))
        return image

    @staticmethod
    def get_apk():
        """
        得到最新的apk
        :return:                       返回最新的apk名字 string类型
        """
        try:
            dirs = os.listdir(global_parameters.apk_path)
            if dirs is not None:
                dirs.sort()
                new_apk = dirs[-1]
                print('最新的apk包为：' + new_apk)
                return new_apk
            else:
                print('This directory is empty')
        except FileNotFoundError as error:
            print(' FileNotFoundError:{0}'.format(error))

    def install_apk(self):
        """
        安装qpk
        :return:
        """
        apk_path = global_parameters.apk_path+'\\'+self.get_apk()
        return self.driver.install_app(apk_path)

    def remove_apk(self, app_id):
        """
        删除apk
        :param app_id:                       apk_id string类型
        :return:
        """
        return self.driver.remove_app(app_id)

    def close_current_window(self):
        """
        关键当前创窗口
        :return:
        """
        return self.driver.close()
