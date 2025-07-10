import xlrd

def getexcel():
    # 打开excel文件
    excel = xlrd.open_workbook('../testdata/uie-nano.xls')
    # 读取excel
    table = excel.sheet_by_index(0)
    rows = table.nrows
    cols = table.ncols
    print(table)
    print(rows)
    print(cols)
    title = table.row(1)[1]
    print(title)
    print("----------------------------------------------")

    for title in range(1,table.nrows):
        title =table.cell_value(title,1)
        print(title)

    for meoth in range(1,table.nrows):
        meoth = table.cell_value(meoth,5)
        print(meoth)

    for url in range(1,table.nrows):
        url = table.cell_value(url,6)
        print(url)

    for header in range(1,table.nrows):
        header = table.cell_value(header,7)
        print(header)

    for datajson in range(1,table.nrows):
        datajson = table.cell_value(datajson,8)
        print(datajson)
        print('-------------------------------------------------')

    return title,meoth,url,header,datajson


