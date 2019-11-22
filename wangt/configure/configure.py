import logging

import requests

from wangt.configure.cookices import Wangt


class Basics(object):
    logging.basicConfig(level=logging.INFO)
    url = "http://t0st.ytzq.com:8443/web/bus/json?"
    cookies = Wangt.get_cookices()
    method = "POST"
    params = {}
    def set_params(self, params):
        self.params = params
        return self

    def run(self):
        self.response = requests.request(
            self.method,
            self.url,
            cookies=self.cookies,
            params=self.params,
        )
        print(self.response)
        return self

    def validate(self, key, expect_value):
        value = self.response.json()
        for _key in key.split("."):
            print("=======", key.split("."))
            if isinstance(value, requests.Response):
                value = getattr(value, _key)
                print("+++++++++", value)
            elif isinstance(value, dict):
                value = value[_key]



        # actual_value = getattr(self.response, key)
        # assert value == expect_value

        return self
