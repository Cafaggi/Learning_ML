#import codecademylib3_seaborn
import seaborn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load and investigate the data here:

df =  pd.read_csv(r"C:\Users\caffa\Desktop\tennis_ace_starting\tennis_ace_starting\tennis_stats.csv")

# perform exploratory analysis here:

features = [
        'Year'
        ,'FirstServe'
        ,'FirstServeReturnPointsWon'
        ,'SecondServePointsWon'
        ,'SecondServeReturnPointsWon'
        ,'Aces'
        ,'BreakPointsConverted'
        ,'BreakPointsFaced'
        ,'BreakPointsOpportunities'
        ,'BreakPointsSaved'
        ,'DoubleFaults'
        ,'ReturnGamesPlayed'
        ,'ReturnGamesWon'
        ,'ServiceGamesPlayed'
        ,'ServiceGamesWon'
        ,'TotalPointsWon'
        ,'TotalServicePointsWon'
        ,'Wins'
        ,'Losses'
        ,'Ranking'
]

y = df[['Winnings']]

lmodel = LinearRegression()

counter = 1

#look for the best linear matchs

print('the most linearly dependent features are:')

for feature in features:
    x = df[feature].values.reshape(-1,1)
    lmodel.fit(x,y)
    if round(lmodel.score(x,y),3) < 0.6:
        continue
    print( feature,'::: coeficent: ', int(lmodel.coef_),', score: ',round(lmodel.score(x,y),3))
    counter +=1

print('''.........................................................
.........................................................
.........................................................''')

## perform single feature linear regressions here:

y = df[['Winnings']]

x = df['BreakPointsOpportunities'].values.reshape(-1,1)


# split 

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

lmodel.fit(x_train,y_train)

#test 1D

print('train_score 1 feature', round(lmodel.score(x_train,y_train),3))

print('test_score 1 feature', round(lmodel.score(x_test,y_test),3))

y_predict = lmodel.predict(x_test)

plt.subplot(311)
plt.xlabel('y_test')
plt.ylabel('y_predict')
plt.title('test_score 1 feature')
plt.scatter(y_test,y_predict,alpha=0.4)


## perform two feature linear regressions here:


x =  df[['BreakPointsOpportunities'
            ,'ReturnGamesPlayed']]

y = df[['Winnings']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

lmodel.fit(x_train,y_train)

print('train_score 2 features', round(lmodel.score(x_train,y_train),3))

print('test_score 2 features', round(lmodel.score(x_test,y_test),3))

y_predict = lmodel.predict(x_test)

plt.subplot(312)
plt.xlabel('y_test')
plt.ylabel('y_predict')
plt.title('test_score 2 features')
plt.scatter(y_test,y_predict,alpha=0.4)

## perform multiple feature linear regressions here:

x =  df[['BreakPointsOpportunities'
            ,'ReturnGamesPlayed'
            ,'Wins'
            ,'DoubleFaults'
            ,'ServiceGamesPlayed'
            ,'ReturnGamesPlayed'
            ,'BreakPointsFaced']]

y = df[['Winnings']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

lmodel.fit(x_train,y_train)

print('train_score n features', round(lmodel.score(x_train,y_train),3))

print('test_score n features', round(lmodel.score(x_test,y_test),3))

y_predict = lmodel.predict(x_test)

plt.subplot(313)
plt.xlabel('y_test')
plt.ylabel('y_predict')
plt.title('test_score n features')
plt.scatter(y_test,y_predict,alpha=0.4)

plt.show()
