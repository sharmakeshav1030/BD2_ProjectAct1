#%%
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [10, 6]
plt.xlabel("Top Items sold")
plt.ylabel("Sales in 2017")

data = pd.read_csv(r"C:\Users\acer\Downloads\BreadBasket_DMS.csv") 
data= data.set_index(['Item'])
data= data.drop(['NONE'])
data.reset_index(inplace = True)


data['Date'] = pd.to_datetime(data['Date'],format='%d-%m-%Y''%d/%m/%Y', errors='coerce')
print(data)
data['weekday'] = data['Date'].dt.dayofweek


weekday= data.set_index(['weekday'])
final=weekday.loc[0]
final.reset_index(inplace = True)

popular=final['Item'].value_counts()
print(popular.head())
mcolor = list('rgbkymc')
popular.head().plot(kind='bar', color=mcolor,width= .9)

plt.show()


# %%
