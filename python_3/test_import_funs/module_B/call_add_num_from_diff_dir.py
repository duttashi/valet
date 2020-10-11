"""
Created on Sun Oct 11 12:02:36 2020
import function from another folder
@author: Ashish
"""

# from tests.module_A.add_num import *
# from ...module_A.add_num import *
# from tests.module_A.add_num import *
from python_3.test_import_funs.module_A.add_num import *
print(add_num(10, 20))