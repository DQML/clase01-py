import pandas as pd

excelData = pd.read_excel('C:/Users/52553/Documents/ebc-python/clase01-py/sample-xls-file-for-testing.xls')
dataFrame = pd.DataFrame(excelData)
print(dataFrame.head())