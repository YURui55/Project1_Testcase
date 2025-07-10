import requests

def test_51job():

    url='https://we.51job.com/api/job/search-pc?api_key=51job&timestamp=1752053381&keyword=%E7%A7%BB%E5%8A%A8%E7%AB%AF%E6%B5%8B%E8%AF%95&searchType=2&function=&industry=&jobArea=000000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum=1&requestId=&pageSize=20&source=1&accountId=198533392&pageCode=sou%7Csou%7Csoulb&scene=7'

    cookies={
        'cookie':'guid=2ecb95bb99ece5e82f0e8e6b9675fb4e; ps=needv%3D0; sensor=createDate%3D2021-10-15%26%7C%26identityType%3D1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22198533392%22%2C%22first_id%22%3A%22196aff4d71c547-0e45cfd1ed51668-4c657b58-3686400-196aff4d71d2c67%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fmail.qq.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk2YWZmNGQ3MWM1NDctMGU0NWNmZDFlZDUxNjY4LTRjNjU3YjU4LTM2ODY0MDAtMTk2YWZmNGQ3MWQyYzY3IiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiMTk4NTMzMzkyIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22198533392%22%7D%2C%22%24device_id%22%3A%22196aff4d71c547-0e45cfd1ed51668-4c657b58-3686400-196aff4d71d2c67%22%7D; Hm_lvt_1370a11171bd6f2d9b1fe98951541941=1751872323; partner=sem_pcbingbd_42560; adv=ad_logid_url%3Dhttps%253A%252F%252Ftrace.51job.com%252Ftrace.php%253Fpartner%253Dsem_pcbingbd_42560%2526ajp%253DaHR0cHM6Ly9ta3QuNTFqb2IuY29tL3RnL3NlbS9scDIwMjUvTFBfMjAyNV9CQzIuaHRtbD9mcm9tPWJpbmdhZCZwYXJ0bmVyPXNlbV9wY2JpbmdiZF80MjU2MA%253D%253D%2526k%253D878e099aee01eaff342a93c50d4e0154%2526msclkid%253D2c14054d6b811010bca06d23461d8b0c%26%7C%26; 51job=cuid%3D198533392%26%7C%26cusername%3DqKcs8wpi4JKSBZdx%252B%252B1lyTgLJyDOU0nyXpEx4YkHB%252Fs%253D%26%7C%26cpassword%3D%26%7C%26cname%3DKjZVPLQIA1DlTgeQXivMHQ%253D%253D%26%7C%26cemail%3DP5H3TP1%252BwWRIFt47%252F9kKCqf44RiWbC2Tzn8Y30GqOQI%253D%26%7C%26cemailstatus%3D3%26%7C%26cnickname%3D%26%7C%26ccry%3D.0jvOyXAAyDCk%26%7C%26cconfirmkey%3D17i9j7.m1EiJw%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D1%26%7C%26cnamekey%3D17Dyu2deLHc8g%26%7C%26to%3Dfbc014afc59d6fb2818187b86dc4facb686e2dd7%26%7C%26; slife=lowbrowser%3Dnot%26%7C%26lastlogindate%3D20250709%26%7C%26securetime%3DAj5XY1Y1B2FXNVRvCTMIYltuCzw%253D; acw_tc=ac11000117520533732333902e0099ca90e0e0f803e6933ecdf396e3c9274f; acw_sc__v2=686e367e8ffd65ceec5e27886d06cd54fd7527fe; JSESSIONID=ABCC4CBD7B729D40F97DE1C9C40A65AA; ssxmod_itna=YqIhqRxAOh0G7iGkDprD+rx9Dfoxl4BtfdGgDYq7=GFKDCh0aSlMrRqDKtqoPpUNezWqDsNBlxGzDikPGhDBnva3DGqU88mAMBqwqmG7BDt80OnygYQYRr2gx9QFPxrRIrV9tUxf2ZLINDB3DbqDytBw//DGGG4GwDGoD34DiDDPAD03Db4D+BmrD7ER=VQn3sm4DQ4GyDitDKw+3xi3DA4Djfl66flF42e5D0q5wgT+fKDGWfnT4sp+7xGt4llh5feDM3xGXBAkCfeDBlKCCYcTL2zO+zjcFxBQD7wFt=QFH0nWiOCOPaG1W050RDfR5BGre41zqxn0Da0q/w7mGxNBqnDxf7N/2D54FDg5DDWsixqirejm7lqXTzcLbydssB+zgQ9mY7rwq0QpE3hxp9Y5MGDagxarq5mqYDxNj+zYpoiDD; ssxmod_itna2=YqIhqRxAOh0G7iGkDprD+rx9Dfoxl4BtfdGgDYq7=GFKDCh0aSlMrRqDKtqoPpUNezlxDWsWiYA4DLlDvmpYx0ywxdo0g3xECDGTTe88/TSDL1OfgxaCHVbixyLFTWzEgLBm9ziMqbp0fj/oQfSSLalYXRKijamGGP=MhpFxx3oiX5BA6563TDrmGynTx3k2NZKGEazYbhA4fFTpfYHrQiLfRj/MxFO3HFsaTFVC=1kOrefeu6m6g8O/fcKBWQacSPuW87o7gFctb8LzoVttd0ucFQ5D0Rv91uOM1ihRN=C5uBGS8glL1LnjNeY=QG8nI=gL27P49U5iEeResPiPGwNlxdI2N7ikmw1Qf5nP=nPQFRhmrxD'
    }
    headers={
        'user-token':'fbc014afc59d6fb2818187b86dc4facb686e2dd7',
        'uuid':'2ecb95bb99ece5e82f0e8e6b9675fb4e',
        #'accept-encoding':'gzip, deflate, br, zstd',
        'account-id':'198533392',
        'property':'%7B%22partner%22%3A%22sem_pcbingbd_42560%22%2C%22webId%22%3A2%2C%22fromdomain%22%3A%2251job_web%22%2C%22frompageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2F%22%2C%22pageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2Fpc%2Fsearch%22%2C%22identityType%22%3A%22%E8%81%8C%E5%9C%BA%E4%BA%BA%22%2C%22userType%22%3A%22%E8%80%81%E7%94%A8%E6%88%B7%22%2C%22isLogin%22%3A%22%E6%98%AF%22%2C%22accountid%22%3A%22198533392%22%2C%22keywordType%22%3A%22%E5%BA%95%E7%BA%B9%E8%AF%8D%22%7D',
        'sign':'411212adba5108f4e9f23d4c9e32994f311605c2574d8a138150f30c9e2e185b'

    }

    resopnse_job=requests.get(url=url,cookies=cookies,headers=headers)
    resopnse_job.encoding='utf8'
    print(resopnse_job.text)
    #print(resopnse_job.encoding)