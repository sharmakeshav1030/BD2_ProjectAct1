#%%
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [10, 6]
plt.xlabel("Week Days")
plt.ylabel("Sales")

data = pd.read_csv(r"C:\Users\acer\Downloads\BreadBasket_DMS.csv") 

data= data.set_index(['Item'])
data= data.drop(['NONE'])
data.reset_index(inplace = True)

bread= data['Item']== 'Bread'
breaddata= data[bread]

breaddata['Date'] = pd.to_datetime(breaddata['Date'],format='%d-%m-%Y', errors='coerce')
breaddata['weekday'] = breaddata['Date'].dt.weekday
sales=breaddata['weekday'].value_counts()
new= sales.sort_index()
renamed= new.rename(index={0:'Monday',1:'Tuesday', 2:'Wednesday',3: 'Thursday', 4:'Friday', 5:'Saturday', 6: 'Sunday'})

print("\nBreads sold per weekday: \n")

print(renamed)

average=renamed.sum()/7
print("\nThe number of average transactions of bread per weekday: " + str(average)+ "\n")

renamed.plot(kind='line', color='red', marker='o')

plt.show()


# %%
