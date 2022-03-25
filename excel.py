import xlrd

try:
    wb = xlrd.open_workbook("C:/Users/crenauro/Documents/selenium_training/users.xls")
    sheet = wb.sheet_by_index(0)
    cnt_row = sheet.nrows
    cnt_col = sheet.ncols
    print(cnt_col)
    print(cnt_row)

    for i in range(1, cnt_row):
        id = sheet.cell_value(i, 0)
        username = sheet.cell_value(i, 1)
        password = sheet.cell_value(i, 2)
        print(id,username, password)

except Exception as e:
    print("Error reading excel")
    print(e)


