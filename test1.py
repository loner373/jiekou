import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests


class test(object):
    url = "http://t0st.ytzq.com:8443/web/bus/json"
    response = requests.post(url,
                             params={
                                 "funNo": "100201",
                                 "login_name": "1300022253",
                                 "img_tiket": "9437",
                                 "safe_type": "1",
                                 "user_agent": "Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64%3B%20rv%3A70.0)%20Gecko%2F20100101%20Firefox%2F70.0",
                                 "request_source": "%E5%A4%96%E5%9B%B4%3A%E5%85%AC%E5%8F%B8%E7%BD%91%E7%AB%99",
                                 "login_password": "3781627eae83b54ce79a9a66f952fca82cc4bf04f31d16ae81ed077dbd39c4c0747245a649e0791ff0f08b48361d6a4c4aa3420a3ce386e1c9a414284beffabf31022b51eb9e831bc07c3c48d8188d8325e3052c1469d57f360ab4e90d14df6e81bc9214b4df7f3369033b5b29350722896c8b1608bb5f4888f7123749c6d833"
                             }

                             )
    print(response.cookies.get_dict())

