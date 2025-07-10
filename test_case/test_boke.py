import requests
import re
from config.sever_boke import severboke

def test_boke():
    # 使用封装好的方法severboke（）
    url=severboke()+'/software-test-Python/p/14464362.html'
    response_boke =requests.get(url=url)
    #用正则表达式提取响应的某个数据
    response_boke_username=re.findall('<h3 id="XI6f6" data-lake-id="96d606e69fea328a398370c14df1e0eb" data-wording="true">(.+?)</h3>',response_boke.text)
    #print(response_boke.text)
    # 打印提取的结果，是列表类型
   # print(response_boke_username)
    # 使用切片标记，提取第一个列表值[0],打印出来
    print(response_boke_username[0])
    return response_boke_username

