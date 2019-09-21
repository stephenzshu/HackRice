import pandas as pd

df = pd.read_excel (r'RiceHackathonFile.xlsx') #for an earlier version of Excel, you may need to use the file extension of 'xls'
print (df)
df2 = pd.read_excel (r'RiceHackathonFile.xlsx', sheet_name='Work Order Examples')
data  = pd.DataFrame(df2,columns= ['Priority(1-5)'])
print (data)