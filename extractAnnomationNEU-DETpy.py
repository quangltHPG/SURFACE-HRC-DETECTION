from bs4 import BeautifulSoup
import os
import pandas as pd
files = os.listdir('./crazing')
resultName = []
resultFilename = []
resultXmin = []
resultYmin = []
resultXmax = []
resultYmax = []
Xmin = []
Ymin = []
Xmax = []
Ymax = []
for file in files:
    file = os.path.join('crazing', file)
    with open(file, 'r') as f:
        data = f.read() 
    bs_data = BeautifulSoup(data, 'xml')   
    b_unique = bs_data.find('filename') 
    b_name = bs_data.find_all('object')
    
    _resultFilename = []
    _resultName = []
    _resultXmin = []
    _resultYmin = []
    _resultXmax = []
    _resultYmax = []    
    for th in b_name:
        _resultName.extend(th.find_all('name'))
        _resultXmin.extend(th.find_all('xmin'))
        _resultYmin.extend(th.find_all('ymin'))
        _resultXmax.extend(th.find_all('xmax'))
        _resultYmax.extend(th.find_all('ymax'))
    for _result in _resultName:
        value = _result.contents[0]
        resultName.append(value)
    for _result in _resultXmin:
        resultFilename.append(b_unique.text.strip())
        value = _result.contents[0]
        Xmin.append(value)
    for _result in _resultYmin:
        value = _result.contents[0]
        Ymin.append(value)
    for _result in _resultXmax:
        value = _result.contents[0]
        Xmax.append(value)
    for _result in _resultYmax:
        value = _result.contents[0]
        Ymax.append(value)
df = pd.DataFrame({
                        'resultFilename':resultFilename,
                        'resultname':resultName,
                        'Xmin':Xmin,
                        'Ymin':Ymin,
                        'Xmax': Xmax,
                        'Ymax':Ymax})
df.to_csv("HRC.csv")