import pandas as pd
datas = pd.read_csv("Z:/collegeThings/Sem5/ML/housing.xls")
data = pd.DataFrame(datas, 14)
data.head()

print(data)
