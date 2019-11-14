import requests
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

class Wangt(object):
    logging.basicConfig(level=logging.DEBUG)
    _join = "登录"
    _customer = "//*[text()='请输入客户代码']"
    _password = "//*[text()='密码']"
    _joinds = "//*[text()='登录']"
    @classmethod
    def get_cookices(cls):
        driver = webdriver.Chrome()
        driver.get("http://t0st.ytzq.com:8443")
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.find_element(By.ID, cls._join)
        driver.find_element(By.ID, cls._join).click()
        driver.implicitly_wait(10)
        conf = yaml.safe_load(open("Wangt.yaml"))
        logging.debug(conf["env"])
        driver.find_element(By.XPATH, cls._customer)
        driver.find_element(By.XPATH, cls._customer).click()
        driver.find_element(By.XPATH, cls._customer).send_keys(conf["env"]["Customer"])
        driver.find_element(By.XPATH, cls._password)
        driver.find_element(By.XPATH, cls._password).click()
        driver.find_element(By.XPATH, cls._password).send_keys(conf["env"]["password"])
        driver.find_element(By.XPATH, cls._joinds).click()
        cookices = driver.get_cookies()
        cls._cookice = cookices
        return cls._cookice