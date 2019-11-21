import json
import logging

from wangt.Business.Jybl import Jyblyw


class TestProtocol(object):
    logging.basicConfig(level=logging.INFO)



    def test_Beiyonglxr(self):
        kwargs = {
                    "funcNo": "100966",
                   "trade_no": "1100004603",
        }
        r = Jyblyw.Beiyong(self, **kwargs)
        logging.info(json.dumps(r.json(), indent=2))
        assert r.json()["results"][0]["linkman_tel"] == "13713727983"

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
        assert r.json()["results"][0]["exp_date"] == "20191114"
        assert r.json()["results"][0]["isOutTime"] == "true"
        assert r.json()["results"][0]["rating_date"] == "20191113"
        assert r.json()["results"][0]["user_role"] == "1"
        assert r.json()["results"][0]["next_rating_date"] == "20191113"
    def test_Kechuangban(self):
        kwargs = {
            "funcNo": "160501",
            "trade_no": "1100004603",
            "trade_account": "1100004603",
            "branch_no" : "0015",
            "ip": "%E5%90%A6",
            #"professional_investor": "%E5%90%A6",
            "source": "2",
            "isktpta": "0",
            "isktxya": "0",
            "sh_a": "A427171551",
            "sh_a_xy": "0",
            "sh_trdacct": "A427171551",
        }
        r = Jyblyw.Beiyong(self, **kwargs)
        logging.info(json.dumps(r.json(), indent=2))
        assert r.json()["results"][0]["exp_date"] == "20191114"
        assert r.json()["results"][0]["isOutTime"] == "true"
        assert r.json()["results"][0]["rating_date"] == "20191113"
        assert r.json()["results"][0]["user_role"] == "1"
        assert r.json()["results"][0]["next_rating_date"] == "20191113"