Calendar-Health Sentiments
====

# About
This project aims to discover how...
- Mood correlates with heart rate?
- Mood correlates with diet?
- Mood correlates with weight?


# TODO
## High-level
- [x] Connect Sentiments API - Google Natural Language API
- [x] Connect Fitbit API (get info from it)
- [x] Connect Google Calendar API
- [ ] Connect D3 / graphing library

## Data
- [ ] Structure the data to compare
- [ ] Compare the data
- [ ] Create graphs
- [ ] Create analysis


# Running the scripts

## Calendar
```
python cal.py
```

## Sentiments
```
python sentiments.py lib/reviews/bladerunner-mixed.txt
```

## Fitbit
1. Go to the OAuth2.0 tutorial page
2. Authorize with Client id, Client secret, and a redirect URI (http://tiffanyqi.com)
3. Parse the response
4. Make the request via Hurl.it
5. Run health.py, replacing the token with the code
	```
	python health.py
	```
