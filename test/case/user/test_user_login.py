import json
import sys
import os
import unittest
import requests

sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))

from basecase import BaseCase

class TestUserLogin(BaseCase):
    def test_user_login_normal(self):
        '''level1:正常登陆'''
        case_data = self.get_case_data("test_user_login_normal")
        self.send_request(case_data)
        
    
if __name__ == "__main__":
    unittest.main()