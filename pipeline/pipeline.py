import sys 
import pandas as pd
file = sys.argv[1]

df = pd.DataFrame({'index':1, 'name':file}, index=[0])
print(df)
print("file name that was passed is : "+ file)
