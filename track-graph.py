# Running
# $ python track-graph.py

import os

# import seaborn as sns
# import matplotlib.pyplot as plt
from datetime import datetime

# sns.set(style="white", context="talk")


def get_day_abbrev(i):
    week = {
        0: "Mon",
        1: "Tue",
        2: "Wed",
        3: "Thu",
        4: "Fri",
        5: "Sat",
        6: "Sun",
    }
    return week.get(i)


def track_graph():

    tracking_by_date = {}

    with open(os.path.expanduser("~") + "/tracking-log.csv", "r") as log:
        logdata = log.readlines()

    log = {}
    for entry in logdata:
        entry = entry.split(",")
        log[entry[0].strip()] = entry[1].strip()

        timestamp = int(entry[0])

        date_key = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")

        if date_key not in tracking_by_date:
            tracking_by_date[date_key] = 0
        tracking_by_date[date_key] += 1

    print(str(tracking_by_date))

    print(len(tracking_by_date))

    weekday_totals = {}
    for i in range(0, 7):
        weekday_totals[i] = {"total": 0, "count": 0, "average": 0}

    for d in tracking_by_date:
        date_parts = d.split("-")
        weekday = datetime(
            int(date_parts[0]), int(date_parts[1]), int(date_parts[2])
        ).weekday()

        # add to totals
        weekday_totals[weekday]["total"] += tracking_by_date[d]
        weekday_totals[weekday]["count"] += 1

        # show some output
        print(d + " -- " + get_day_abbrev(weekday) + " -- " + "X" * tracking_by_date[d])
        if weekday == 4:
            print()

    for i in weekday_totals:
        if weekday_totals[i]["count"] > 0:
            weekday_totals[i]["average"] = round(
                weekday_totals[i]["total"] / weekday_totals[i]["count"], 2
            )
    print(weekday_totals)
    for i in weekday_totals:
        print(get_day_abbrev(i) + ":  " + str(weekday_totals[i]))

    # print(
    #     datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
    #     + " -- "
    #     + entry[1]
    # )

    # for entry in log:
    #     print(entry + '   ' + log[entry])

    # x = log.keys()
    # print(x)
    # graph.savefig('graph.png')


if __name__ == "__main__":
    track_graph()