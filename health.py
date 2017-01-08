import requests
import json
import pandas as pd
from time import sleep

# from: http://shishu.info/2016/06/how-to-download-your-fitbit-second-level-data-without-coding/

# put the token for your app in between the single quotes
token = ''

# make a list of dates
# ref: http://stackoverflow.com/questions/993358/creating-a-range-of-dates-in-python
# You can change the start and end date as you want
# Just make sure to use the yyyy-mm-dd format
start_date = '2015-08-10'
end_date = '2017-01-07'
datelist = pd.date_range(start=pd.to_datetime(start_date),
                         end=pd.to_datetime(end_date)).tolist()

'''
The codes below use a for loop to generate one URL for each day in the datelist,
and then request each day's data and save the data into individual json files.
Because Fitbit limit 150 request per hour, I let the code sleep for 30 seconds
between each request, to meet this limitation.
'''
for ts in datelist:
    date = ts.strftime('%Y-%m-%d')
    url = 'https://api.fitbit.com/1/user/-/activities/heart/date/' + date + '/1d/1sec/time/00:00/23:59.json'
    filename = 'HR' + date + '.json'
    response = requests.get(url=url, headers={'Authorization': 'Bearer ' + token})

    if response.ok:
        with open(filename, 'w') as f:
            json.dump(response.content, f)
        print (date + ' is saved!')
        sleep(30)
    else:
        print ('The file of %s is not saved due to error!' % date)
        sleep(30)
