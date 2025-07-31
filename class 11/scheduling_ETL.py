import datetime, timedelta
import pandas as pd
from datetime import datetime, timedelta
import time

def extractor():
    column = ['target','id','date','flag','user','text']
    df = pd.read_csv('data.csv',encoding='latin1',names = column)
    print(df)
    return df

def trasformation(df):
    df['sentiment'] = df['target'].map({0: 'negative', 2: 'neutral', 4: 'positive'})
    return df

def loading(df):
    df.to_csv('new.csv', index = False)

def etl_pipline():
    data = extractor()
    new_data = trasformation(data)
    loading(new_data)

def time_threshold():
    now = datetime.now()
    print(now)
    threshold_time = now.replace(hour=12, minute=38, second=0, microsecond=0)
    threshold_time = now.replace(hour=12, minute=39, second=0, microsecond=0)
    
    print(threshold_time)
    if now>threshold_time:
        threshold_time = threshold_time + timedelta(1)
        print("th",threshold_time)
    print("thr__",(threshold_time - now).total_seconds())
    return (threshold_time-now).total_seconds()


def scheduler():
    while True:
        moment = time_threshold()
        time.sleep(moment)
        etl_pipline()
        print("done")
scheduler()