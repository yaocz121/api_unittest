import sys
import unittest
import time
import pickle
import click

from lib.HTMLTestReportCN import HTMLTestRunner
from config.config import *
from lib.send_email import send_email



def discover():
    return unittest.defaultTestLoader.discover(test_case_path)

def run_all():  # 运行所用用例
    run(discover())


def collect():
    suite = unittest.TestSuite()

    def _collect(tests):
        if isinstance(tests,unittest.TestSuite):
            if tests.countTestCases() != 0:
                for i in tests:
                    _collect(i)
        else:
            suite.addTest(tests)
    
    _collect(discover())
    return suite

def collect_only():
    t0 = time.time()
    i = 0
    for case in collect():
        i+=1
        print("{},{}".format(str(i),case.id()))
        print("----------------------------------------------------------------------")
        print("Collect {} tests is {:.3f}s".format(str(i),time.time()-t0))



def save_failures(result,file):
    suite = unittest.TestSuite()
    for case_result in result.failures:
        suite.addTest(case_result[0])

    with open(file,'wb') as f:
        pickle.dump(suite,f)

def rerun_fails():
    sys.path.append(test_case_path)
    with open(last_fails_file,'rb') as f:
        suite = pickle.load(f)
    run(suite)

def run(suite):
    logging.info("================================== 测试开始 ==================================")
    
    with open(report_file,'wb') as f:
        result = HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="yaocz").run(suite)

    if result.failures:
        save_failures(result,last_fails_file)
    
    if send_email_after_run:
        send_email(report_file)

    logging.info("================================== 测试结束 ==================================")



@click.command()
@click.option("--collect",default=None,help="输入：collect 查看所有用例")
@click.option("--rerun",default=None,help="输入：rerun 运行上次失败的用例")
def main(collect,rerun):
    if collect == "collect":
        collect_only()
    elif rerun == "rerun":
        rerun_fails()
    else:
        run_all()

if __name__ == "__main__":
    main()