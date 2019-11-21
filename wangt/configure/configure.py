import logging

import requests

from wangt.configure.cookices import Wangt


class Configure(object):

    url = "http://t0st.ytzq.com:8443/web/bus/json?"
    cookies = Wangt.get_cookices()
    params = {}

    def run(self):
        self.response = requests.post(self.url, cookies=self.cookies, params=self.params)
        return self

    def validate(self, key, expect_value):
        actual_value = getattr(self.response, key)
        assert actual_value == expect_value
        return self