from wangt.cookices import Wangt
import requests


class Jyblyw(object):
    @classmethod
    def setup_class(cls):
        Wangt.get_cookices()
        print(Wangt.get_cookices())
    def Beiyong(self, **kwargs ):
        url = "http://t0st.ytzq.com:8443/web/bus/json?"
        return requests.get(url,
                            params=kwargs,
                            # params={
                            #     "funcNo": "100966",
                            #     "trade_no": "1100004603",
                            # },
                            cookies=Wangt.get_cookices()
                            )
