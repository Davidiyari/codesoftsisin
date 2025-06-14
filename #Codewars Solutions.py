#Codewars Solutions
def calculate(s):
    return str(eval(s.replace("plus", "+").replace("minus", "-")))

import codewars_test as test
from solution import calculate

