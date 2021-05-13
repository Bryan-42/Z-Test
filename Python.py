import random
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

data = pd.read_csv("medium_data.csv")

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

    population_mean = mean

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    means.append(mean_list)

def show_fig(mean_list):
    df = mean_list
    fig = go.create_distplot([df], ["temp"], show_hist = False)
    fig.show()

std_deviation = statistics.stdev(means)

z_score = (means - mean)/std_deviation
print("the z score is = ", z_score)