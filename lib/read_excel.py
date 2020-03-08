import xlrd
import os
import sys
sys.path.append('../..')
from config.config import *


def excel_to_list(data_file,sheet):
    data_list = []
    wb = xlrd.open_workbook(data_file)
    sh = wb.sheet_by_name(sheet)
    header = sh.row_values(0)
    for i in range(1,sh.nrows):
        d = dict(zip(header,sh.row_values(i)))
        data_list.append(d)
    return data_list

def get_test_data(data_list,case_name):
    for case_data in data_list:
        if case_name == case_data['case_name']:
            return case_data


if __name__ == '__main__':
    data_list = excel_to_list('test_user_data.xlsx','TestUserLogin')
    case_data = get_test_data(data_list,'test_user_login')
    print(case_data)
    

