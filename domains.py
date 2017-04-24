import pandas as pd
import read
from collections import Counter

domains = read.load_data()
s = domains['url'].str.cat(sep=' ')
s = s.lower()

urls = s.split(' ')
urlCount = Counter(urls)

url_keys = list(urlCount.keys())
url_values = list(urlCount.values())

rows = list()
rows.append(url_keys)
rows.append(url_values)
headers = rows.pop(0)

url_df = pd.DataFrame(rows, columns=headers)
url_df = url_df.transpose()
url_df.columns = ["Frequency"]
url_df = url_df.sort('Frequency',ascending=False)
'''url_df = url_df.drop(url_df.index[7])
print(url_df.head(5))'''

indexes = list(url_df.index.values)
counter = 0
top_list = []
for index in indexes:
    if counter < 100:
        top_list.append(index)
        counter += 1
        
print(top_list)