import statistics
from plotly import colors
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import random

df = pd.read_csv('data.csv')
data = df['reading_time'].tolist()

population_mean = statistics.mean(data)

def randomSetOfMean(counter):
    dataset = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def showFigure(meanList):
    df = meanList
    #mean = statistics.mean(df)
    fig = ff.create_distplot([df],['reading_time'], show_hist=False)
    fig.show()

meanList = []
for i in range(0,100):
    setOfMeans = randomSetOfMean(30)
    meanList.append(setOfMeans)

sd = statistics.stdev(meanList)
mean = statistics.mean(meanList)

firstStdDeviationStart, firstStdDeviationEnd = mean-sd, mean + sd
secondStdDeviationStart, secondStdDeviationEnd = mean-(2*sd), mean + (2*sd)
thirdStdDeviationStart, thirddStdDeviationEnd = mean-(3*sd), mean + (3*sd)

newmeanList = []
for i in range(0,200):
    setOfMeans = randomSetOfMean(30)
    newmeanList.append(setOfMeans)

newMean = statistics.mean(newmeanList)

fig = ff.create_distplot([meanList],['reading_time'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode = 'lines', name = 'Mean'))
fig.add_trace(go.Scatter(x=[newMean,newMean],y=[0,0.17],mode = 'lines', name = 'New Mean'))
fig.add_trace(go.Scatter(x=[firstStdDeviationStart,firstStdDeviationStart],y=[0,0.17],mode = 'lines', name = 'first'))
fig.add_trace(go.Scatter(x=[firstStdDeviationEnd,firstStdDeviationEnd],y=[0,0.17],mode = 'lines', name = 'first'))
fig.add_trace(go.Scatter(x=[secondStdDeviationStart,secondStdDeviationStart],y=[0,0.17],mode = 'lines', name = 'second'))
fig.add_trace(go.Scatter(x=[secondStdDeviationEnd,secondStdDeviationEnd],y=[0,0.17],mode = 'lines', name = 'second'))
fig.add_trace(go.Scatter(x=[thirdStdDeviationStart,thirdStdDeviationStart],y=[0,0.17],mode = 'lines', name = 'third'))
fig.add_trace(go.Scatter(x=[thirddStdDeviationEnd,thirddStdDeviationEnd],y=[0,0.17],mode = 'lines', name = 'third'))
fig.show()

zScore = (newMean - mean)/sd
print(zScore)




