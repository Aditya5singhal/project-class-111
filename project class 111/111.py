import pandas as pd
import plotly.figure_factory as px
import plotly.graph_objects as px1
import csv
import statistics
import random
df=pd.read_csv('School1.csv')
data=df['Math_score'].tolist()

#fig=px.create_distplot([data],['average'],show_hist=False)
#fig.show()


dataset=[]
for i in range(0,100):
    randomnos=random.randint(0,len(data)-1)
    value=data[randomnos]
    dataset.append(value)
mean1=statistics.mean(dataset)
print(mean1)
stdiv1=statistics.stdev(dataset)
print(stdiv1)
fig=px.create_distplot([dataset],['dataset'],show_hist=False)


fig.show()




df=pd.read_csv('data3.csv')
data=df['Math_score'].tolist()

#fig=px.create_distplot([data],['average'],show_hist=False)
#fig.show()


dataset=[]
for i in range(0,100):
    randomnos=random.randint(0,len(data)-1)
    value=data[randomnos]
    dataset.append(value)
mean2=statistics.mean(dataset)
print(mean2)
stdiv2=statistics.stdev(dataset)
print(stdiv2)
fig=px.create_distplot([dataset],['dataset'],show_hist=False)
#fig2=px1.scatter([dataset],['dataset'],show_hist=False)
#fig2.show()
fig.show()




df=pd.read_csv('studentMarks.csv')
data=df['Math_score'].tolist()

#fig=px.create_distplot([data],['average'],show_hist=False)
#fig.show()


dataset=[]
for i in range(0,100):
    randomnos=random.randint(0,len(data)-1)
    value=data[randomnos]
    dataset.append(value)
mean3=statistics.mean(dataset)
print(mean3)
stdiv3=statistics.stdev(dataset)
print(stdiv3)
fig=px.create_distplot([dataset],['dataset'],show_hist=False)
#fig2=px1.scatter([dataset],['dataset'],show_hist=False)
#fig2.show()
fig.show()

z_score=(mean1-mean2)/stdiv1
print(z_score)

z_score2=(mean1-mean3)/stdiv1
print(z_score2)

z_score3=(mean3-mean2)/stdiv3
print(z_score3)