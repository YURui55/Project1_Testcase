import pytest
import  requests
import xlrd

def testbubei():
    read_excel = xlrd.open_workbook('../testdata/不背测试用例.xls')
    table01 = read_excel.sheet_by_index(0)
    print(table01)
    # 第一行第一列的值
    print(table01.cell_value(0,0))
    #输出第一行的数据-标题
    print(table01.row_values(0))
    # 输出第二行的数据-值
    print(table01.row_values(1))
    print("----------------------------------------------------------")
    # 拼接标题与数据组装成字典
    print(dict(zip(table01.row_values(0),table01.row_values(1))))
    print("----------------------------------------------------------")
    # 读取标题
    table01_biaoti=table01.row_values(0)
    print(table01_biaoti)
    print("----------------------------------------------------------")
    print("----------------------------------------------------------------")

    data_shuju_list=[]
    for i in range(1,table01.nrows): # 读取值
        #print(table01.row_values(i))
        # 拼接标题与值,字典形式
        data_shuju=dict(zip(table01_biaoti,table01.row_values(i)))
        #print(data_shuju)
        # 外套列表格式，将字典加入到列表中
        data_shuju_list.append(data_shuju)
        print(data_shuju_list)
    return data_shuju_list

# 获取excel测试数据，进行请求测试
# pytest参数化
@pytest.mark.parametrize('test',testbubei())
def test_case_excelbubei(test):
    #print("当前用例",test)
    response = requests.request(
        url=test['url'],
        method=test['method'],
        params=eval(test['data']),
    )

    print('接口响应',response.text)
    # 断言
    assert eval(test['expect']) == eval(response.content.decode('utf-8')), "断言失败，实际结果与预期结果不一致"
    #




