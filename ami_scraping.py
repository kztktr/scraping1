# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

class WebAccess: 
    site_url = None
    user_id = None
    user_password = None
    driver = None

    # constract(initialization) 
    def __init__(self, val, user_id, user_password): 
    print('-- init WebAccess --') 
    self.site_url = val
    self.user_id = user_id
    self.user_password = user_password
    print('site_url:', self.site_url)
    print('user_id:', self.user_id)
    print('user_password:', self.user_password)

    # Destructor
    def __del__(self):
        print("-- del WebAccess -- ")
        self.driver.quit()
    del self.site_url, self.user_id, self.user_password, self.driver

def main():
    print('Hello!') 
    # ------------------------------------------------- 
    # 初期値の読み込み 
    # ------------------------------------------------- 
    site_url = 'hoge.com' ## 対象ページurl 
    user_id, user_password = 'id xxxxxxx', 'pass xxxxxxxxx' ## id と パスワード
    # ------------------------------------------------- 
    # クラス生成
    # ------------------------------------------------- 
    web_ac = WebAccess(site_url, user_id, user_password) 