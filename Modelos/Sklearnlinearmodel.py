import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression

a = {'a':[1,3,5],'b':[4,4,6]}
df = pd.DataFrame(a)

X = df['a']
X = X.values.reshape(-1,1)

y = df['b']
y = y.values.reshape(-1,1)

reg = LinearRegression()
reg.fit(X,y)

new_y = reg.predict(X)

plt.scatter(X,y)
plt.plot(X,new_y)
plt.show()