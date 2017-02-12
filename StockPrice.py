import pandas as pd
import pandas_datareader.data as web
import datetime
import sqlite3

def makedatetime(starttime,endtime):
    start = datetime.datetime(starttime[0],starttime[1],starttime[2])
    end = datetime.datetime(endtime[0],endtime[1],endtime[2])
    print(start)

if __name__ == '__main__':
    starttime = [2010, 1, 1]
    endtime = [2011, 1, 1]
