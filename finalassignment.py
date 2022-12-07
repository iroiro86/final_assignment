import pandas as pd
import numpy as np
import matplotlib as plt

df=pd.read_csv("finance_liquor_sales_test.csv")
cn=df.groupby('zip_code')
d=cn.aggregate(np.sum)/47

print(d)

#plt.show()
#print (cn.aggregate(np.sum))
