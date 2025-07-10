import pytest
if __name__=="__main__":
    #运行测试用例-这个目录下的以test开头，-test结尾的
    #pytest.main(['../test_case'])


    #生成测试报告，报告类型+报告地址，
    # 01:--html=../report/report.html
    # 02:--junitxml=../report/report.xml
    # 03:allure目录，json格式
    #   '--alluredir','../report/reportallure'
    pytest.main(['../test_case','--html=../report/report.html','--junitxml=../report/report.xml','--alluredir','../report/reportallure'])
