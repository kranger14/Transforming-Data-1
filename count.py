from collections import Counter
import io
import read
import pandas as pd
df = read.load_data()

s = df['headline'].str.cat(sep=' ')
s = s.lower()

words = s.split(" ")
wordCount = Counter(words)

WCkeys = list(wordCount.keys())
WCvalues = list(wordCount.values())

rows = list()
rows.append(WCkeys)
rows.append(WCvalues)
headers = rows.pop(0)

WCdf = pd.DataFrame(rows, columns=headers)
WCdf = WCdf.transpose()
WCdf.columns = ["Frequency"]
WCdf = WCdf.sort('Frequency',ascending=False)
WCdf = WCdf.drop(WCdf.index[7])
'''print(WCdf.head(5))'''

indexes = list(WCdf.index.values)
counter = 0
top_list = []
for index in indexes:
    if counter < 100:
        top_list.append(index)
        counter += 1
        
print(top_list)