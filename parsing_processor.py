import pandas as pd
import sys, importlib

try:
    importlib.reload(sys.modules['hh_parser'])
except:
    pass
from hh_parser import hh_parser

while True:
    try:
        pages = int(input('Specify number of pages to parse info from:'))
        break
    except ValueError:
        print("Please enter an integer.")

data = pd.DataFrame(columns=['name', 'xp_req', 'remote', 'company', 'description'])
    
for i in range(0, pages, 3):
    df = hh_parser(i, min(i+3, pages))
    data = pd.concat([data, df], ignore_index=True)
    
data.to_json('data.json')