#%%
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [10, 6]
plt.xlabel("Date")
plt.ylabel("Sales")


data = pd.read_csv(r"C:\Users\acer\Downloads\BreadBasket_DMS.csv") 

data['Date'] = pd.to_datetime(data['Date'],format='%d-%m-%Y', errors='coerce')
data['year'] = data['Date'].dt.year

lol= data.loc[data['year'] == 2017]


# items = seventeen.set_index(['Item'])
# NewItems= items.drop(['NONE'])
# NewItems.reset_index(inplace = True)

# data with only item coffee
coffee= lol.set_index(['Item'])
onlycoffee= coffee.loc['Coffee']
onlycoffee.reset_index(inplace = True)

# display the dates with total transactions
popular=onlycoffee['Date'].value_counts()

print("\nTop 5 dates on which sales of coffee was highest: \n")
print("Date          Total")
print(popular.head())

popular.head().plot(kind='line', color='blue', marker='o')
plt.title("Top 5 sales day for coffee")
plt.show()

# %%
