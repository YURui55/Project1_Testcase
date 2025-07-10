

# 封装博客的ip
def severboke():
    # 使用字典格式进行参数化{‘字段1’：‘值’}
    sever_boke01 ={
        'sevet_boke_test':'https://www.cnblogs.com',
        'sevet_boke_dev': 'https://www.cnblogs11111.com'
    }
    # return sever_boke01['sevet_boke_test']

    # 使用列表格式进行参数化[‘值1’，‘值2’]
    sever_boke02=['https://www.cnblogs.com','https://www.cnblogs11111.com']

    return sever_boke02[0]