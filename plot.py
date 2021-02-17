import matplotlib.pyplot as plt
import matplotlib
import japanize_matplotlib
import json
import random

json_open = open('festa/festa_d.json', 'r')
json_load = json.load(json_open)

for noun in json_load:
    x = range(len(json_load[noun]))
    adjective_dict = json_load[noun]
    fig = plt.figure(figsize=(20, 20))
    
    height = []
    labels = []

    keys = adjective_dict.keys()
    for key in keys:
      labels.append(key)
      height.append(adjective_dict[key])
    bar = plt.bar(x, height, tick_label = labels, width=0.5, color="b")
    plt.title(noun, fontsize=40)
    # plt.xticks(rotation=90)
    plt.tick_params(labelsize=40)
    plt.grid(True)
    fig.savefig(f"{noun}.png")