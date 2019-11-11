import json
import logging
import pytest
import hamcrest
import requests


class TestRequest(object):
    logging.basicConfig(level=logging.INFO)
    url = "http://t0st.ytzq.com:8443/web/bus/json?"

    def test_cookices(self):
        r = requests.post(self.url,
                          params={
                              "funcNo":"160101",
                              "trade_no": "1300022253",
                              "branch_no": "0013",
                              "user_agent":"Mozilla%252F5.0%2520(Windows%2520NT%25206.1%253B%2520Win64%253B%2520x64%253B%2520rv%253A70.0)%2520Gecko%252F20100101%2520Firefox%252F70.0"
                                },
                          headers = {
                              "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0",
                              "Accept": "application/json, text/javascript, */*; q=0.01",
                                     },

                          cookies={
                              "JSESSIONID": 'abc5FroUrMiKz5FBun04w',
                              "sso_cookie": "3o%2F%2BqYJWo0hM8VKiISsYJw%2F5EGb%2F620DXhi1ZTIatEb6B3a9VMbvRyRLYla6Txp7fq6f6sp8u0Si%0A5qjOfoRcJEYvlbpPGFQ8O0kr1VLS7u0Cn1N9bTFT4CtBZgg1wcxdGvgH8BkwIvGz2l2YZL5rNgQ0%0AbTkg4HiscFEUBgh%2B0FOhIzmZRCHr%2FFawvNbJcrN2Q4OYDXyNqYpEic5nrsX3mNM1uCxX8WUsb3Tn%0AgrIdP1qqXjDhfakJQFIPiJjlwffJ7CRDqc8JTQhNJWEjtLgEFUOw%2FscTR92RV9c9wNHhYF6z5oDP%0ALIsoHjOyjq9stWusJ3B6LW%2BKZgaiq64DVwAz%2BV%2Fusi8kIVkrN5Zn5IXb3xtAXEosvRsSAPzBiPHu%0AheketX9mNHo1dboMqbL0VvXht%2FdyeORDFXlwrBpqtail02elI53RQcjb6ai4h17L6LyQPwah1yZH%0ADcZKk%2FoVVqpfEevGCrq6Qk8HyndR7CzKr431FqS8XcVmBw9AgBEQmJuhRaEyjr9ezDSd2VxOj3L4%0AR0yPbxvVIghg3d%2BMFuj8GBGXmcYJvAtHNKGZe2%2FYaX%2F6s5KPt9Pns71OB%2Fw6Zix%2B5kpHNdXhDa%2F%2F%0A%2FDcFuDhUz8jqeO4j5qXjhS8pfOfkqNc9yQX4Xggj5uYLZ69G%2BAuR1LEJQqZg6OVEq2xA2ptr%2FDtc%0AVEDJ2f4wJBobnkgfcturrbeMl%2BurIHXJuHi64BXXB1C0jd6J0kWaXl1ij0AEXoR8iy48Wl%2FPP%2FlR%0ADrfdNJi4mNbr0XfF7QfHecxEkN1yNUcXCsb%2F0YrJqAmwwSSncj1solFv1d3SMjE2KTBk%2F5RIRXOz%0AnXKcGjJjsRwhTxgpSvCRZ3tDdy3PKcs9wMag012GNy6s0Uu%2FtVtmsr0eRl6WoendmcXjdj4x6%2FAM%0AFPvpQrbI2UvMrsAH%2Fi5NnHwezJtJ4StY9hpAKWTyOCACSW7%2FTNU7JkArQ9JXW9wsQ73iLSv3Elbp%0Ay6NTvk3VnXtg%2BkV9XvMt1N9uJ%2BO7HHcUz2r0W6y7RLtjYdYpW4DMe%2F5AtMm0DJiKh37F8%2BF1ONV7%0AfGG0VcFt5cRU75s%2FeSxJ1ODzWK7kAPNisvo%3D",
                              "info": "%7B%22sfbd%22:%221%22,%22rzrq_creditAccount%22:%221390000235%22,%22net_addr%22:%22text%252Fhtml%253B%2520charset%253DUTF-8%22,%22crm_name%22:%22%E9%99%88%E8%BE%89%22,%22trade_account%22:%221300022253%22,%22crm_no%22:%226423083%22,%22trade_name%22:%22%E9%99%88%E8%BE%89%22,%22branch_no%22:%220013%22,%22device_info%22:%22Mozilla/5.0%20(Windows%20NT%206.1@#@%20Win64@#@%20x64@#@%20rv:70.0)%20Gecko/20100101%20Firefox/70.0%22,%22crm_client_type%22:%220%22,%22identity_exp_date%22:%2220260812%22,%22branch_name%22:%22%E4%B8%8A%E6%B5%B7%E5%98%89%E5%96%84%E8%B7%AF%E8%AF%81%E5%88%B8%E8%90%A5%E4%B8%9A%E9%83%A8%22,%22trade_no%22:%221300022253%22,%22wealth_product%22:%22%22,%22wealth_level%22:%220%22,%22identity_idno%22:%22310230197711013718%22%7D",
                              "preChangeCard": "%7B%221300022253%22:%7B%22balance%22:%221.485756024E7%7C1.484624121E7%22,%22flow_create_date%22:%222019-08-01%2011:22:04%22,%22flow_status%22:%22%22,%22contract_status%22:%220%22,%22flag%22:false,%22main_flag%22:%221%22,%22cuacct_status%22:%220%22,%22bank_acct%22:%226222031001001920003%22,%22ext_org%22:%222003%22,%22isSuccess%22:false,%22cuacct_code%22:%221300022253%22,%22yzflag%22:false%7D%7D",
                              "tradeAccount": "1300022253",
                              "indexFlag": "sug_attend",
                              "investor":"%7B%22risklevelvaliddate%22:%2220211025%22,%22investmentperiod%22:%222%22,%22lowriskflag%22:%220%22,%22investmenttype%22:%2202%22,%22exincometype%22:%22%22,%22risklevel%22:%224%22,%22trdprofvaliddate%22:%223000/12/31%22,%22investortype%22:%220%22,%22riskpropright%22:%224%22%7D' --data-binary",

                              },
                          )
        #logging.info(r.text)
        #logging.info(json.dumps(r.json(), indent=2))
        assert r.json()["results"][0]["mobile_tel"] == "18926080076"
