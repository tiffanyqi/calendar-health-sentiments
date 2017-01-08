import requests
import json
import pandas as pd
from time import sleep

# from: http://shishu.info/2016/06/how-to-download-your-fitbit-second-level-data-without-coding/

token = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIzUDZWTjMiLCJhdWQiOiIyMjg2UDciLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcmFjdCBybG9jIHJ3ZWkgcmhyIHJudXQgcnBybyByc2xlIiwiZXhwIjoxNDg0NDYzNjY0LCJpYXQiOjE0ODM5MTc1Nzh9.j81zU_ShCahOnjJl3J7EChCMvEgWjz5agnwvAylYyqs'
# start_date = '2015-08-21'
start_date = '2017-01-06'
end_date = '2017-01-07'
datelist = pd.date_range(start=pd.to_datetime(start_date),
                         end=pd.to_datetime(end_date)).tolist()

# fitbit api requests
information = {
    'heartrate': {
        'url': 'https://api.fitbit.com/1/user/-/activities/heart/date/',
        'filename': 'HR-',
        'date': '/1d/1sec/time/00:00/23:59.json'
    },
    'sleep': {
        'url': 'https://api.fitbit.com/1/user/-/sleep/date/',
        'filename': 'Sleep-',
        'date': '.json'
    },
    'food': {
        'url': 'https://api.fitbit.com/1/user/-/foods/log/date/',
        'filename': 'Calories-',
        'date': '.json'
    },
    'weight': {
        'url': 'https://api.fitbit.com/1/user/-/body/log/weight/date/',
        'filename': 'Weight-',
        'date': '.json'
    }
}

for ts in datelist:
    date = ts.strftime('%Y-%m-%d')

    for key in information:
        api = information[key]
        url = api.get('url') + date + api.get('date')
        filename = api.get('filename') + date + '.json'

        response = requests.get(url=url, headers={'Authorization': 'Bearer ' + token})

        if response.ok:
            # request each day's data, save it in individual json files
            with open(filename, 'w') as f:
                json.dump(response.content, f)
            print (key + ' for ' + date + ' is saved to ' + filename)
            sleep(30)
        else:
            print ('The file of %s is not saved due to error!' % url)
