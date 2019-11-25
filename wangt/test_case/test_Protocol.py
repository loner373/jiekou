from wangt.Business.Jybl import Jyblyw
from wangt.configure.configure import Basics


class TestProtocol(Basics):
    def test_Beiyonglxr(self):
        params = Jyblyw.Beiyong(self)
        TestProtocol \
            .set_params(self, params) \
            .run() \
            .validate("status_code", 200) \
            .validate("json().results.linkman_mobile_tel", "18926080076") \
            .validate("json().results.linkman_tel", "18926080076")

    def test_Chaxunsfz(self):
        kwargs = {
            "funcNo": "160101",
            "trade_no": "1100004603"
        }
        TestProtocol \
            .set_params(self, kwargs) \
            .run() \
            .validate("json().results.mobile_tel", "18926080076")

    def test_Chaxunfxcp(self):
        params = {
            "funcNo": "160102",
            "trade_no": "1100004603",
            "crm_client_type": "0",
        }
        TestProtocol \
            .set_params(self, params) \
            .run() \
            .validate("status_code", 200) \
            .validate("json().results.exp_date", "20211114") \
            .validate("json().results.isOutTime", "false") \
            .validate("json().results.rating_date", "20191115") \
            .validate("json().results.next_rating_date", "20191115")

    def test_Kechuangban(self):
        params = {
            "funcNo": "160501",
            "trade_no": "1100004603",
            "trade_account": "1100004603",
            "branch_no": "0015",
            "ip": "%E5%90%A6",
            # "professional_investor": "%E5%90%A6",
            "source": "2",
            "isktpta": "0",
            "isktxya": "0",
            "sh_a": "A427171551",
            "sh_a_xy": "0",
            "sh_trdacct": "A427171551",
        }
        TestProtocol \
            .set_params(self, params) \
            .run() \
            .validate("status_code", 200) \
            .validate("json().results.trading_expr", "7816") \
            .validate("json().results.sfdz", "0") \
            .validate("json().results.isTime", "0") \
            .validate("json().results.tm", "0")
