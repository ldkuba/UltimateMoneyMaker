import datetime
import pandas as pd
import os.path
from forex_python.converter import get_rate
import time
from multiprocessing import Process 

def updateDataThreading (counter, startTime, endTime):
    while (endTime.timestamp () != startTime.timestamp ()):
        with open (str (counter) + '.csv', 'a') as f:
            try:
                rate = get_rate ('GBP', 'USD', startTime)
                f.write (str (startTime.timestamp ()) + ',' + str (startTime) + ',' + str (rate) + '\n')
                startTime += datetime.timedelta (hours = 1)
                print (rate)
            except Exception as e:
                pass
#                                          Change these numbers!
updateDataThreading (1, datetime.datetime (2003, 1, 1), datetime.datetime (2004, 1, 1))
