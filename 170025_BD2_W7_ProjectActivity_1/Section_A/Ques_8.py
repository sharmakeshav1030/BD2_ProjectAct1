#%%
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r"C:\Users\acer\Downloads\BreadBasket_DMS.csv")

#Removing NONE values
data= data.set_index(['Item'])
data= data.drop(['NONE'])
data.reset_index(inplace = True)

#finding out the Frequency
#first we will locate all the transactions done with coffee.
comb= data.loc[data['Item'] == 'Coffee', ['Transaction']]

#we will replace the new transaction ids with old ones and change the items accoringly
new= data['Transaction'].isin(comb['Transaction'])
data['Item']=data[new]

# we will also remove all the NaN values that has emerged due to lack of transaction Id.
newData= data.dropna()

# we will also remove Item Coffee to have a precise data set of items brought togethor with Coffee.
newData= newData.set_index(['Item'])
newData= newData.drop(['Coffee'])
newData.reset_index(inplace = True)
print("\n Filtered Data set :\n")
print(newData)

# Now we will find the frequency of the items and plot the graph accordingly.

popular=newData['Item'].value_counts()
Frequency= popular/len(newData)
print("\n Frequency of Items purchased with Coffee\n")
print(Frequency)

Frequency.head().plot(kind='bar',x='name',y='age')

print("\n \n Best item combination with coffee based on the frequency is bread Because it has been brought maximum number  times with Coffee. \n Cake, Tea, Pastry, Sandwich and medialuna can be consider good pairs with coffee because they are in the top 5 list of items transacted with coffee.\n \n")

plt.show()
# %%
