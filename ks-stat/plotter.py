import pandas
import matplotlib.pyplot as plt
from scipy import stats

df1 = pandas.read_csv("experiments.csv")
df1['experiments'].plot(kind='bar')

df11 = pandas.DataFrame(data={
    'df1': df1['experiments']
})

df11.plot.kde()

#plt.plot(df1['experiments'])
plt.show()

d1 = df11['df1']

print(stats.kstest(d1, 'norm', (d1.mean(), d1.std()), N=5000))
