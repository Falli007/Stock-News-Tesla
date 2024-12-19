import requests




STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
Stock_API_KEY = " 60KUXXYJWV6ZIIOT"
News_API_KEY = "c05088c3976e4ffd856d9f53960d5e9a"


## Step 1: Use https://www.alphavantage.co/documentation/#daily
#When the stock price increases/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# 1. Get yesterday's closing stock price.
stocks_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": Stock_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stocks_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)
    
# 2. Get the day before yesterday's closing stock price.
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# 3. Find the positive difference between 1 and 2. e.g. 40 - 20 = 20
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

# 4. Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (difference / float(yesterday_closing_price)) * 100
print(diff_percent)

# 5. If TODO4 percentage is greater than 5 then print("Get News").
if diff_percent > 5:
    print("Get News")

# 6. Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if diff_percent > 5:
    news_params = {
        "apiKey": News_API_KEY,
        "qInTitle": COMPANY_NAME,    
    }
    
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)  
    articles = news_response.json()["articles"]
    print(articles)
   

# 7. Use the python slice operator to create a list that contains the first 3 articles  https://newsapi.org/docs/endpoints/everything
three_articles = articles[:3]
print(three_articles)
# 8. Create a new list of the first 3 articles headline and description using list comprehension.
# 9. Send each article as a separate message on the phone number.
     