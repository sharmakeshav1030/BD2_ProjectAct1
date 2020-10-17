#%%
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [10, 5]
plt.xlabel("Hours")
plt.ylabel("Sales")
data = pd.read_csv(r"C:\Users\acer\Downloads\BreadBasket_DMS.csv")

data= data.set_index(['Item'])
data= data.drop(['NONE'])
data.reset_index(inplace = True)

data['Time'] = pd.to_datetime(data['Time'],format= '%H:%M:%S', errors='coerce')
data['hour'] = data['Time'].dt.hour
popular=data['hour'].value_counts()
print("\nNumber of sales per hour:  \n")
print(popular.sort_index())

average=popular.sum()/24
print("The number of average transactions per hour: " + str(average))

popular.sort_index().plot(kind='bar', color='blue')


plt.show()



# %%
