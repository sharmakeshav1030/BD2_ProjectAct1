#%%
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\Keshav\Downloads\BreadBasket_DMS.csv") 

data= data.set_index(['Item'])
filtered= data.drop(['NONE'])
data= data.reset_index()
filtered= filtered.reset_index()
transaction_list = []

# For loop to create a list of the unique transactions throughout the dataset:
for i in filtered['Transaction'].unique():
    tlist = list(set(filtered[filtered['Transaction']==i]['Item']))
    if len(tlist)>0:
        transaction_list.append(tlist)


te = TransactionEncoder()
te_ary = te.fit(transaction_list).transform(transaction_list)
df2 = pd.DataFrame(te_ary, columns=te.columns_)

frequent_itemsets = apriori(df2, min_support=0.01, use_colnames=True)
#take minimum threshold
rules = association_rules(frequent_itemsets, metric='lift')

rules.sort_values('confidence', ascending=False)
print("Rules:\n")
print(rules.head(5))
print("\n")
#now categorise every rule with different range of confidence
rules['support']= rules['support']*100
rules['confidence']= rules['confidence']*100
rules['lift']= rules['lift']
rules2= rules[['antecedents','consequents', 'support', 'confidence','lift']]

# rules2= rules2[rules2.confidence > 50]

rules2= rules2.sort_values('confidence', ascending=False)
print("pairs with best confidence: \n")
print(rules2.head())
print("\n")
rules2= rules2.sort_values('support', ascending=False)
print("pairs with best support: \n")
print(rules2.head())
print("\n")
print("As We can see from the above tables, The best possible pairs would be Cake & Coffee, Paestry & Cake\n")
rules2= rules2.sort_values('confidence', ascending=False)
print("pairs with worst confidence: \n")
print(rules2.tail())
print("\n")
rules2= rules2.sort_values('lift', ascending=False)
print("pairs with best lift: \n")
print(rules2.head())
print("\n")
rules2= rules2.sort_values('lift', ascending=False)
print("pairs with worst lift: \n")
print(rules2.tail())
print("\n")

rules3=rules2.set_index('confidence')

rules4= rules3.sort_index()
finalrules=rules4.reset_index()
finalrules["antecedents"] = finalrules["antecedents"].apply(lambda x: list(x)[0]).astype("unicode")
finalrules["consequents"] = finalrules["consequents"].apply(lambda x: list(x)[0]).astype("unicode")

finalrules['combination']= finalrules['antecedents']+" And " + finalrules['consequents']
finalrules= finalrules.drop_duplicates()
print("All the pairs with minimum support their confidence: \n")
finalrules.plot(x='combination', y= 'confidence',kind='bar', color='blue')
plt.rcParams["figure.figsize"] = [10, 6]
plt.xlabel("Item Pairs")
plt.ylabel("Confidence(%)")
plt.title("Optimal Pairs wrt optimal support-confidence")
plt.show()

# %%
