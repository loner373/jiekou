import json
import logging
import pytest

import requests


class TestProtocol(object):
    logging.basicConfig(level=logging.INFO)

    # @classmethod
    # def setup_class(cls):
    #     Wangt.get_cookices()
    #     print(Wangt.cookices)
    url = "http://t0st.ytzq.com:8443/web/bus/json?"
    def test_Beiyonglxr(self):

        r = requests.get(self.url,
                         params={
                             "funcNo": "100966",
                             "trade_no": "1100004603",
                         },
                         cookies={
                             "JSESSIONID": 'abc5FroUrMiKz5FBun04w',
                             "sso_cookie": "3o%2F%2BqYJWo0gv92GU7c6Npw%2F5EGb%2F620DXhi1ZTIatEblgaLD%2FP5eKNn3yVpUD%2FDLyBpe848S%2Bb3%2B%0AidD%2F0RirxVW6VVw7IYj5m4mY4yFjFJWEx5Lo25PE5fxOeY13tIly7XCa767coUbsR9%2FbVS4m2tqo%0AWtqvLHl90Nyk5a0JhCTTNbgsV%2FFlLG9054KyHT9aY0T37TTm3%2BlSD4iY5cH3yewkQ6nPCU0IUbl1%0Aw6qVwkWGE%2BCVQZiQHzjyqwWAWfnN5iCXBcA7O9L1XqMZZIEW3ZIcYZ6OOhX4aI553AppoV3CIiTL%0A%2FyvMHl%2FO4ElUwqaQ8EPpoMxjoSPLnB9ZWFfUmRKIIMSyM6nQMGWjYDXYp%2FVLeInn08RA%2F6Dy49ZD%0AxtrtVW42dgADOGPkEumcA3PtPh%2FXuvjUlsiVoh8APYoabOWHZ%2FbWv11IRBakohTlOlpZ%2Bm%2BE2lkJ%0A7VSlcXFz8C7DjbysATl1oS7DeS3shJ95Ze4MfcBvKn5PfEZDAl1tRd4ZGzRU4Gi2W18S6xseC5aU%0AVc6btK5Gmc%2B4hAPQPBuNuQE9Y65Wew%2BBBvw3Bbg4VM%2FI6njuI%2Bal44VdpvpsvDlRLskF%2BF4II%2Bbm%0AC2evRvgLkdSxCUKmYOjlRKtsQNqba%2Fw7XFRAydn%2BMCQaG55IH3Lbq623jJfrqyB1ybh4uuAV1wdQ%0AtI3eidJFml5dYo9ABF6EfIsuPFpfzz%2F5UQ633TSYuJjW69F3xe0Hx3nMRJDdcjVHFwrG%2F9GKyagJ%0AsMEkp3I9bKJRb9Xd0jLahckXl6ImcUVzs51ynBoyRcEWB8NvkvKcC5Yr6pfda%2FcE1iu0GAjYhjcu%0ArNFLv7VbZrK9HkZelqHp3ZnF43Y%2B7XCa767coUbsR9%2FbVS4m2v4uTZx8HsybSeErWPYaQClk8jgg%0AAklu%2F0zVOyZAK0PSV1vcLEO94i0r9xJW6cujU75N1Z17YPpFfV7zLdTfbifjuxx3FM9q9Fusu0S7%0AY2HWKVuAzHv%2BQLTJtAyYiod%2BxU%2F9B0JyaTetZofZXAHSYwXsVIioBKjvVViu5ADzYrL6",
                             "info": "%7B%22sfbd%22:%220%22,%22rzrq_creditAccount%22:%220%22,%22net_addr%22:%22text%252Fhtml%22,%22crm_name%22:%22%E9%99%88%E5%86%9B%22,%22trade_account%22:%221100004603%22,%22crm_no%22:%2213812%22,%22trade_name%22:%22%E9%99%88%E5%86%9B%22,%22branch_no%22:%220012%22,%22device_info%22:%22Mozilla/5.0%20(Windows%20NT%206.1@#@%20Win64@#@%20x64@#@%20rv:70.0)%20Gecko/20100101%20Firefox/70.0%22,%22crm_client_type%22:%220%22,%22identity_exp_date%22:%2220260619%22,%22branch_name%22:%22%E6%B7%B1%E5%9C%B3%E5%BD%A9%E7%94%B0%E8%B7%AF%E8%AF%81%E5%88%B8%E8%90%A5%E4%B8%9A%E9%83%A8%22,%22trade_no%22:%221100004603%22,%22wealth_product%22:%22%22,%22wealth_level%22:%220%22,%22identity_idno%22:%22440921197405118336%22%7D",
                         },
                         )

        logging.info(json.dumps(r.json(), indent=2))
        assert r.json()["results"][0]["linkman_tel"] == "13713727983"

    def test_Chaxunsfz(self):
        r = requests.get(
            self.url,
            params={
                "funcNo": "160101",
                "trade_no": "1100004603"
            },
            cookies = {
                      "JSESSIONID": 'abc5FroUrMiKz5FBun04w',
                      "sso_cookie": "3o%2F%2BqYJWo0gv92GU7c6Npw%2F5EGb%2F620DXhi1ZTIatEblgaLD%2FP5eKNn3yVpUD%2FDLyBpe848S%2Bb3%2B%0AidD%2F0RirxVW6VVw7IYj5m4mY4yFjFJWEx5Lo25PE5fxOeY13tIly7XCa767coUbsR9%2FbVS4m2tqo%0AWtqvLHl90Nyk5a0JhCTTNbgsV%2FFlLG9054KyHT9aY0T37TTm3%2BlSD4iY5cH3yewkQ6nPCU0IUbl1%0Aw6qVwkWGE%2BCVQZiQHzjyqwWAWfnN5iCXBcA7O9L1XqMZZIEW3ZIcYZ6OOhX4aI553AppoV3CIiTL%0A%2FyvMHl%2FO4ElUwqaQ8EPpoMxjoSPLnB9ZWFfUmRKIIMSyM6nQMGWjYDXYp%2FVLeInn08RA%2F6Dy49ZD%0AxtrtVW42dgADOGPkEumcA3PtPh%2FXuvjUlsiVoh8APYoabOWHZ%2FbWv11IRBakohTlOlpZ%2Bm%2BE2lkJ%0A7VSlcXFz8C7DjbysATl1oS7DeS3shJ95Ze4MfcBvKn5PfEZDAl1tRd4ZGzRU4Gi2W18S6xseC5aU%0AVc6btK5Gmc%2B4hAPQPBuNuQE9Y65Wew%2BBBvw3Bbg4VM%2FI6njuI%2Bal44VdpvpsvDlRLskF%2BF4II%2Bbm%0AC2evRvgLkdSxCUKmYOjlRKtsQNqba%2Fw7XFRAydn%2BMCQaG55IH3Lbq623jJfrqyB1ybh4uuAV1wdQ%0AtI3eidJFml5dYo9ABF6EfIsuPFpfzz%2F5UQ633TSYuJjW69F3xe0Hx3nMRJDdcjVHFwrG%2F9GKyagJ%0AsMEkp3I9bKJRb9Xd0jLahckXl6ImcUVzs51ynBoyRcEWB8NvkvKcC5Yr6pfda%2FcE1iu0GAjYhjcu%0ArNFLv7VbZrK9HkZelqHp3ZnF43Y%2B7XCa767coUbsR9%2FbVS4m2v4uTZx8HsybSeErWPYaQClk8jgg%0AAklu%2F0zVOyZAK0PSV1vcLEO94i0r9xJW6cujU75N1Z17YPpFfV7zLdTfbifjuxx3FM9q9Fusu0S7%0AY2HWKVuAzHv%2BQLTJtAyYiod%2BxU%2F9B0JyaTetZofZXAHSYwXsVIioBKjvVViu5ADzYrL6",
                      "info": "%7B%22sfbd%22:%220%22,%22rzrq_creditAccount%22:%220%22,%22net_addr%22:%22text%252Fhtml%22,%22crm_name%22:%22%E9%99%88%E5%86%9B%22,%22trade_account%22:%221100004603%22,%22crm_no%22:%2213812%22,%22trade_name%22:%22%E9%99%88%E5%86%9B%22,%22branch_no%22:%220012%22,%22device_info%22:%22Mozilla/5.0%20(Windows%20NT%206.1@#@%20Win64@#@%20x64@#@%20rv:70.0)%20Gecko/20100101%20Firefox/70.0%22,%22crm_client_type%22:%220%22,%22identity_exp_date%22:%2220260619%22,%22branch_name%22:%22%E6%B7%B1%E5%9C%B3%E5%BD%A9%E7%94%B0%E8%B7%AF%E8%AF%81%E5%88%B8%E8%90%A5%E4%B8%9A%E9%83%A8%22,%22trade_no%22:%221100004603%22,%22wealth_product%22:%22%22,%22wealth_level%22:%220%22,%22identity_idno%22:%22440921197405118336%22%7D",
                  },

        )
        logging.info(json.dumps(r.json(), indent=2))
        assert r.json()["results"][0]["mobile_tel"] == "18926080076"

    def test_Chaxunfxcp(self):
        r= requests.get(
            self.url,
            params={
                "trade_no": "1100004603",
                "crm_client_type": "0",
                "funcNo": "160102"
            },
            cookies = {
                      "JSESSIONID": 'abc5FroUrMiKz5FBun04w',
                      "sso_cookie": "3o%2F%2BqYJWo0gv92GU7c6Npw%2F5EGb%2F620DXhi1ZTIatEblgaLD%2FP5eKNn3yVpUD%2FDLyBpe848S%2Bb3%2B%0AidD%2F0RirxVW6VVw7IYj5m4mY4yFjFJWEx5Lo25PE5fxOeY13tIly7XCa767coUbsR9%2FbVS4m2tqo%0AWtqvLHl90Nyk5a0JhCTTNbgsV%2FFlLG9054KyHT9aY0T37TTm3%2BlSD4iY5cH3yewkQ6nPCU0IUbl1%0Aw6qVwkWGE%2BCVQZiQHzjyqwWAWfnN5iCXBcA7O9L1XqMZZIEW3ZIcYZ6OOhX4aI553AppoV3CIiTL%0A%2FyvMHl%2FO4ElUwqaQ8EPpoMxjoSPLnB9ZWFfUmRKIIMSyM6nQMGWjYDXYp%2FVLeInn08RA%2F6Dy49ZD%0AxtrtVW42dgADOGPkEumcA3PtPh%2FXuvjUlsiVoh8APYoabOWHZ%2FbWv11IRBakohTlOlpZ%2Bm%2BE2lkJ%0A7VSlcXFz8C7DjbysATl1oS7DeS3shJ95Ze4MfcBvKn5PfEZDAl1tRd4ZGzRU4Gi2W18S6xseC5aU%0AVc6btK5Gmc%2B4hAPQPBuNuQE9Y65Wew%2BBBvw3Bbg4VM%2FI6njuI%2Bal44VdpvpsvDlRLskF%2BF4II%2Bbm%0AC2evRvgLkdSxCUKmYOjlRKtsQNqba%2Fw7XFRAydn%2BMCQaG55IH3Lbq623jJfrqyB1ybh4uuAV1wdQ%0AtI3eidJFml5dYo9ABF6EfIsuPFpfzz%2F5UQ633TSYuJjW69F3xe0Hx3nMRJDdcjVHFwrG%2F9GKyagJ%0AsMEkp3I9bKJRb9Xd0jLahckXl6ImcUVzs51ynBoyRcEWB8NvkvKcC5Yr6pfda%2FcE1iu0GAjYhjcu%0ArNFLv7VbZrK9HkZelqHp3ZnF43Y%2B7XCa767coUbsR9%2FbVS4m2v4uTZx8HsybSeErWPYaQClk8jgg%0AAklu%2F0zVOyZAK0PSV1vcLEO94i0r9xJW6cujU75N1Z17YPpFfV7zLdTfbifjuxx3FM9q9Fusu0S7%0AY2HWKVuAzHv%2BQLTJtAyYiod%2BxU%2F9B0JyaTetZofZXAHSYwXsVIioBKjvVViu5ADzYrL6",
                      "info": "%7B%22sfbd%22:%220%22,%22rzrq_creditAccount%22:%220%22,%22net_addr%22:%22text%252Fhtml%22,%22crm_name%22:%22%E9%99%88%E5%86%9B%22,%22trade_account%22:%221100004603%22,%22crm_no%22:%2213812%22,%22trade_name%22:%22%E9%99%88%E5%86%9B%22,%22branch_no%22:%220012%22,%22device_info%22:%22Mozilla/5.0%20(Windows%20NT%206.1@#@%20Win64@#@%20x64@#@%20rv:70.0)%20Gecko/20100101%20Firefox/70.0%22,%22crm_client_type%22:%220%22,%22identity_exp_date%22:%2220260619%22,%22branch_name%22:%22%E6%B7%B1%E5%9C%B3%E5%BD%A9%E7%94%B0%E8%B7%AF%E8%AF%81%E5%88%B8%E8%90%A5%E4%B8%9A%E9%83%A8%22,%22trade_no%22:%221100004603%22,%22wealth_product%22:%22%22,%22wealth_level%22:%220%22,%22identity_idno%22:%22440921197405118336%22%7D",
                  },
        )
        logging.info(json.dumps(r.json(),indent=2))

