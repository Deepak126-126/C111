import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium.csv")
data = df["reading_time"].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)

std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("Mean of sampling distribution:- ",mean)
print("Standard Deviation of sampling distribution:- ", std_deviation)

fsds,fsde = mean - std_deviation , mean + std_deviation
ssds , ssde = mean - (2*std_deviation) , mean + (2*std_deviation)
tsds,tsde = mean - (3*std_deviation) , mean + (3*std_deviation)

df = pd.read_csv("medium.csv")
data = df["reading_time"].tolist()
mean_of_sample1 = statistics.mean(data)
print("Mean of sample1: ",mean_of_sample1)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD MATH LABS"))
fig.add_trace(go.Scatter(x=[fsde,fsde], y=[0,0.17], mode="lines", name = "Standard Deviation 1 End"))
fig.add_trace(go.Scatter(x=[ssde,ssde], y=[0,0.17], mode="lines", name = "Standard Deviation 2 End"))
fig.add_trace(go.Scatter(x=[tsde,tsde], y=[0,0.17], mode="lines", name = "Standard Deviation 3 End"))
fig.show()

z_score = (mean - mean_of_sample1)/std_deviation
print("The Z-Score is ",z_score)