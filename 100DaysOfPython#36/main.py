from datetime import datetime
import requests

STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"
TIME = datetime.now().date()

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API = "MB3XJSNTXYUQ0Y48"
NEWS_API = "d18fe55c6554420db932aed7633f4620"

stock_params = {
    "function" : "TIME_SERIES_INTRADAY",
    "symbol" : STOCK,
    "interval" : "30min",
    "apikey" : STOCK_API
}
news_params = {
    "q" : "apple",
    "from" : TIME,
    "sortBy" : "popularity",
    "apikey" : NEWS_API,
    "language" : "en"
}

stock_response = requests.get(url= STOCK_ENDPOINT, params= stock_params)
news_response = requests.get(url= NEWS_ENDPOINT, params= news_params)

stock_data = stock_response.json()
news_data = news_response.json()

yesterday_price = stock_data["Time Series (30min)"]["2022-06-29 16:00:00"]["4. close"]
tdb_yesterday_price = stock_data["Time Series (30min)"]["2022-06-28 16:00:00"]["4. close"]
article_title = news_data["articles"][0]["title"]
article_description = news_data["articles"][0]["description"]


if abs((float(tdb_yesterday_price) - float(yesterday_price)) / float(tdb_yesterday_price) * 100) >= 1:
    print(f"Title : {article_title}\nDescription : {article_description}")