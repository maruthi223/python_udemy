import requests

response =requests.get(url='https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=L3Y2Z7JWAKUUW5DF')
response.raise_for_status()
data = response.json()
close_9 = data['Time Series (Daily)']["2023-08-09"]['4. close']
close_8 = data['Time Series (Daily)']["2023-08-08"]['4. close']
# close_7 = data['Time Series (Daily)']["2023-08-07"]['4. close']
diff = float(close_9) - float(close_8)
percent = (abs(diff)/float(close_9))*100
if percent > 2:
    print('get news')
#news
res = requests.get(url='https://newsapi.org/v2/everything?q=tesla&from=2023-08-8&sortBy=publishedAt&apiKey=56623c2d40a746759c1a935d55b15e8a')
res.raise_for_status()
new_data = res.json()
article = new_data['articles'][3]
