from wangt.configure.configure import Basics


class Jyblyw(Basics):
    url = "http://t0st.ytzq.com:8443/web/bus/json?"
    method = "post"
    params = {
        "funcNo": "100966",
        "trade_no": "1100004603",
    }


class Chaxunsfz(Basics):
    url = "http://t0st.ytzq.com:8443/web/bus/json?"
    method = "post"
    params = {
        "funcNo": "160101",
        "trade_no": "1100004603"
    }


class Chaxunfxcp(Basics):
    url = "http://t0st.ytzq.com:8443/web/bus/json?"
    method = "get"
    params = {
        "funcNo": "160102",
        "trade_no": "1100004603",
        "crm_client_type": "0",
    }


class Kechuangban(Basics):
    url = "http://t0st.ytzq.com:8443/web/bus/json?"
    method = "get"
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