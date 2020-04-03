# Running
# $ python track-graph.py

import os
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

sns.set(style="white", context="talk")

def track_graph():
    
    with open(os.path.expanduser('~')+'/tracking-log.csv', 'r') as log:
        logdata = log.readlines()

    log = {}
    for entry in logdata:
        entry = entry.split(',')
        log[entry[0].strip()] = entry[1].strip()
        
        timestamp = int(entry[0])


        print(datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S') + ' -- '+ entry[1])

    


    # for entry in log:
    #     print(entry + '   ' + log[entry])

    #x = log.keys()
    #print(x)
    #graph.savefig('graph.png')



if __name__ == "__main__":
    track_graph()