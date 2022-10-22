# Running
# $ python track.py <task>

import sys
import os
import datetime

def track():
    with open(os.path.expanduser('~')+'/tracking-log.csv', 'a') as log:
        stamp = int(datetime.datetime.utcnow().timestamp())
        log.write(str(stamp) + ', ' +sys.argv[1] + '\n')



if __name__ == "__main__":
    track()
