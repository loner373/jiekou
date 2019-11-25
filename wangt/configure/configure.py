import logging

import requests

from wangt.configure.cookices import Wangt


class Basics(object):
    logging.basicConfig(level=logging.INFO)
    url = ""
    cookies = Wangt.get_cookices()
    method = ""
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
        value = self.response
        for _key in key.split("."):
            if isinstance(value, requests.Response):
                if _key in ["json()", "json"]:
                    value = self.response.json()
                    print("++++++++", value)
                else:
                    value = getattr(value, _key)
            elif isinstance(value, dict):
                value = value[_key]
                if isinstance(value, list):
                    value = value[0]
        print("----------------", value)
        assert value == expect_value
        return self
