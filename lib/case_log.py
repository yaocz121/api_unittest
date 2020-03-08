
import json
import sys

sys.path.append('../..')

from config.config import *

def log_case_info(case_name,url,data,expect_res,res_text):
    if isinstance(data,dict):
        data = json.dumps(data, ensure_ascii=False)
    logging.info('测试用例：{}'.format(case_name))

    