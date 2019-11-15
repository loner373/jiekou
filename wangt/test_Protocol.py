import json
import logging
import pytest

import requests

from wangt.Jybl import Jyblyw
from wangt.cookices import Wangt


class TestProtocol(object):
    logging.basicConfig(level=logging.INFO)



    def test_Beiyonglxr(self):
        kwargs = {
                    "funcNo": "100966",
                   "trade_no": "1100004603",
        }
        r = Jyblyw.Beiyong(self, **kwargs)
        logging.info(json.dumps(r.json(), indent=2))
        assert r.json()["results"][0]["linkman_tel"] == "18926080076"

    def test_Chaxunsfz(self):
        kwargs = {
            "funcNo": "160101",
            "trade_no": "1100004603"
        }
        r = Jyblyw.Beiyong(self, **kwargs)
        logging.info(json.dumps(r.json(), indent=2))
        assert r.json()["results"][0]["mobile_tel"] == "18926080076"

    # @pytest.mark.parametrize("ziduan","velus", [
    #         ("exp_date", "true"),
    #         ("rating_date", "20191113"),
    #         ("exp_date", "20191114"),
    #         ("isOutTime", "true"),
    #         ("isOneOutTime", "false")
    #     ])
    def test_Chaxunfxcp(self):
        kwargs = {
            "trade_no": "1100004603",
            "crm_client_type": "0",
            "funcNo": "160102",
        }
        r = Jyblyw.Beiyong(self, **kwargs)
        logging.info(json.dumps(r.json(), indent=2))
        assert r.json()["results"][0]["exp_date"] == "20191027"