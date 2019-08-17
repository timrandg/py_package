import pandas as pd
import os

try:
    #line below finds path to this directory dynamically (won't     #matter where on the machine this module is moved).
    fn = os.path.join(os.path.dirname(__file__), 'oscar_male.csv')
    a_df = pd.read_csv(fn)
except:
    print('failed case from local file')

a_str = "Although Python’s extensive standard library covers many programming needs, there often comes a time when you need to add some new functionality to your Python installation in the form of third-party modules. This might be necessary to support your own programming, or to support an application that you want to use and that happens to be written in Python."

a_list = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

def a_function():
    print('I am a_function living in tools.py')
