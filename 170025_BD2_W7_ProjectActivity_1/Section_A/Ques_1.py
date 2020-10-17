
#%%
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [10, 6]
plt.xlabel("Items")
plt.ylabel("Sales")

data = pd.read_csv(r"C:\Users\acer\Downloads\BreadBasket_DMS.csv") 

#Now we will firstchange index to item to sort items into new datasets without 'NONE' type of Items.
items = data.set_index(['Item'])
NewItems= items.drop(['NONE'])
NewItems.reset_index(inplace = True)

#after reseting the index, we will count the items and print the frequency of top 10 selling items.
Top=NewItems['Item'].value_counts()
print("\nFrequency of top 10 selling items: \n")
print(Top.head(10))

Top.head(10).plot(kind='bar', color='red')
plt.show()


# %%
