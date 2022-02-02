import pandas as pd
from datetime import datetime as dt

def preprocessor(data):
    df = pd.read_json(data)
    df1 = df['messages']
    date = []
    user = []
    mes = []
    for i in range(len(df1)):
        dte = df1[i]['date'][0:10] + " " + df1[i]['date'][11:]
        date.append(dte)
        try:
            auth = df1[i]['author']
            user.append(auth)
        except:
            user.append(df1[i]['actor'])
        mes.append(str(df1[i]['text']))
        df = pd.read_csv('dat.csv', index_col=False)
    df['date'] = date
    df['user'] = user
    df['message'] = mes
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%d %H:%M')
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['month_name'] = df['date'].dt.month_name()
    df['day_name'] = df['date'].dt.day_name()
    return df
