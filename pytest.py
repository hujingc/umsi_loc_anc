import requests
import pandas as pd
import numpy as np
import csv # For passwords
#https://couchdb3.prtd.app/_utils/

test = csv.reader('passwords.csv')
#test = csv.read_html('passwords.csv')
print(test)
r = requests.get(url = "https://en.wikipedia.org/wiki/Cat")
print(r)