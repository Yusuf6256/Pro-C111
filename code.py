import csv
import plotly.figure_factory as pf
import plotly.graph_objects as pg
import pandas as pd
import statistics
import random

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

population_mean = statistics.mean(data)
print("The population mean is: ",population_mean)

population_std_dev = statistics.stdev(data)
print("The standard deviation of population is: ",population_std_dev)

fig=pf.create_distplot([data],["Math_score"],show_hist=False)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean


mean_list=[]
for i in range(0,1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)



mean= statistics.mean(mean_list)
print("The mean of sampling distribution is:-",mean)



mean_list=[]
for i in range(0,1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)

sample_std_dev= statistics.stdev(mean_list)
print("The standard deviation of sampling distribution is:-",sample_std_dev)

# #plotting the mean of the sampling
fig = pf.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(pg.Scatter(x=[mean, mean], y=[0, 0.20], mode="lines", name="MEAN"))
print("Standard deviation of sampling distribution:- ", sample_std_dev)

## findig the standard deviation starting and ending values

# finding the mean of the first data(STUDENTS WHO pgT TABLET WITH LEARNING MATERIAL) and plotting it on the plot.
# df = pd.read_csv("data1.csv")
# data = df["Math_score"].tolist()
# mean_of_sample1 = statistics.mean(data)
# print("Mean of sample1:- ",mean_of_sample1)
# fig = pf.create_distplot([mean_list], ["student marks"], show_hist=False)
# fig.add_trace(pg.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
# fig.add_trace(pg.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN OF SAMPLE"))
# fig.add_trace(pg.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
# fig.show(), mean+sample_std_dev
first_std_dev_start, first_std_dev_end = mean-sample_std_dev
second_std_dev_start, second_std_dev_end = mean-(2*sample_std_dev), mean+(2*sample_std_dev)
third_std_dev_start, third_std_dev_end = mean-(3*sample_std_dev), mean+(3*sample_std_dev)
print("std1",first_std_dev_start, first_std_dev_end)
print("std2",second_std_dev_start, second_std_dev_end)
print("std3",third_std_dev_start,third_std_dev_end)

## plotting the graph with traces
fig = pf.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(pg.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(pg.Scatter(x=[first_std_dev_start, first_std_dev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(pg.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(pg.Scatter(x=[second_std_dev_start, second_std_dev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START"))
fig.add_trace(pg.Scatter(x=[second_std_dev_end, second_std_dev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(pg.Scatter(x=[third_std_dev_start,third_std_dev_start], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 START"))
fig.add_trace(pg.Scatter(x=[third_std_dev_end,third_std_dev_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 END"))

# finding the mean of the first data(STUDENTS WHO GOT TABLET WITH LEARNING MATERIAL) and plotting it on the plot.
df = pd.read_csv("data1.csv")
data = df["Math_score"].tolist()
mean_of_sample1 = statistics.mean(data)
print("Mean of sample1:- ",mean_of_sample1)
fig = pf.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(pg.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(pg.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN OF SAMPLE"))
fig.add_trace(pg.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.show()