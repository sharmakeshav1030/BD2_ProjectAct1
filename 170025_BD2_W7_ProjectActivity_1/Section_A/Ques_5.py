#%%
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [10, 5]
plt.xlabel("Months")
plt.ylabel("Sales")

data = pd.read_csv(r"C:\Users\acer\Downloads\BreadBasket_DMS.csv") 

data= data.set_index(['Item'])
data= data.drop(['NONE'])
data.reset_index(inplace = True)
data['Date'] = pd.to_datetime(data['Date'],format='%d-%m-%Y', errors='coerce')
data['month'] = data['Date'].dt.month
sales=data['month'].value_counts()
new= sales.sort_index()

renamed= new.rename(index={1:'January',2:'Febrary', 3:'March',4: 'April', 5:'May', 6:'June', 7: 'July',8:'August', 9:'September',10: 'October', 11:'November', 12:'December'})


print(renamed)


average=renamed.sum()/7
print("\nThe number of average transactions per month: " + str(average))

renamed.plot(kind='bar', color='blue')
plt.show()

# %%
