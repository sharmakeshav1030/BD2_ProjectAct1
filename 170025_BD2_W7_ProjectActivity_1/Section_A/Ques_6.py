#%%
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [10, 5]
plt.xlabel("Week days")
plt.ylabel("Sales")
data = pd.read_csv(r"C:\Users\acer\Downloads\BreadBasket_DMS.csv") 

data= data.set_index(['Item'])
data= data.drop(['NONE'])
data.reset_index(inplace = True)

data['Date'] = pd.to_datetime(data['Date'],format='%d-%m-%Y', errors='coerce')
data['weekday'] = data['Date'].dt.weekday
sales=data['weekday'].value_counts()
new= sales.sort_index()
renamed= new.rename(index={0:'Monday',1:'Tuesday', 2:'Wednesday',3: 'Thursday', 4:'Friday', 5:'Saturday', 6: 'Sunday'})

print(renamed)

average=renamed.sum()/7
print("The number of average transactions per weekday: " + str(average))

renamed.plot(kind='line', color='red', marker='o')

plt.show()

# %%
