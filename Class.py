import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 


data = pd.read_csv('tips.csv')

 #2 . Added calculated column
data["Tips_as_%_of_bill"] = data['tip']/ data["total_bill"] *100
print(data)

#3. Subset of Dinner Data
subset= data[data.time == 'Dinner']
print(subset)


#4. Correlation
corr = subset["tip"].corr(subset["size"])
print("the correllation coefficient between table size and tip is:" )
print(corr)

#5. Data visualisation
thursday = data[data.day =='Thur']
friday = data[data.day =='Fri']
saturday= data[data.day =='Sat']
sunday = data[data.day =='Sun']

plt.bar("thursday",np.sum(thursday["tip"]))
plt.bar("friday",np.sum(friday["tip"]))
plt.bar("saturday",np.sum(saturday["tip"]))
plt.bar("sunday",np.sum(sunday["tip"]))
plt.xlabel("Day")
plt.ylabel("Total Tips")
plt.title("Total tips per day")

plt.show()



