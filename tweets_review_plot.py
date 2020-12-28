import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('tweets.csv')
print(df.head())
df_ = df.groupby(['Sentiment_name']).count()
print(df_)
fig = plt.figure(figsize =(10, 7)) 
plt.pie(df_['Sentiment'], labels = df_.index.values,autopct='%1.2f%%') 
plt.title('Sentiment analysis on Twitter tweets of \'Tata motors customer service\'.')
# show plot 
plt.savefig('pie_chart.png')