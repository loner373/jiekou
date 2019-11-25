from wangt.Business.Jybl import *


class TestProtocol(object):
    def test_Beiyonglxr(self):
        Jyblyw()\
            .run()\
            .validate("status_code", 200)\
            .validate("json().results.linkman_mobile_tel", "18926080076") \
            .validate("json().results.linkman_tel", "18926080076")

    def test_Chaxunsfz(self):
        Chaxunsfz()\
            .run() \
            .validate("status_code", 200) \
            .validate("json().results.mobile_tel", "18926080076")
    def test_Chaxunfxcp(self):
        Chaxunfxcp()\
            .run() \
            .validate("status_code", 200) \
            .validate("json().results.exp_date", "20211114") \
            .validate("json().results.isOutTime", "false") \
            .validate("json().results.rating_date", "20191115") \
            .validate("json().results.next_rating_date", "20191115")

    def test_Kechuangban(self):
        Kechuangban()\
            .run() \
            .validate("status_code", 200) \
            .validate("json().results.trading_expr", "7816") \
            .validate("json().results.sfdz", "0") \
            .validate("json().results.isTime", "0") \
            .validate("json().results.tm", "0")
