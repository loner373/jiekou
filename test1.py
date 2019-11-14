import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class test(object):
    url = "http://t0st.ytzq.com:8443"
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(url)
    driver.maximize_window()
    # search_window0=driver.current_window_handle
    # print(search_window0)
    driver.find_element_by_link_text("登录")
    driver.find_element_by_link_text("登录").click()

    driver.implicitly_wait(10)

    # driver.switch_to_window(driver.window_handles[1])
    # search_window = driver.current_window_handle
    # print(search_window)
    # handles = driver.window_handles
    # print(type(handles))
    # time.sleep(3)
    # driver.switch_to_window(search_window)
    driver.find_element_by_xpath("//*[text()='请输入客户代码']")
    driver.find_element_by_xpath("//*[text()='请输入客户代码']").click()


