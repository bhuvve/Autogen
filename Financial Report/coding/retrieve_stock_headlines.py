# filename: retrieve_stock_headlines.py
import requests
from bs4 import BeautifulSoup

def get_news_headlines(stock_name):
    headlines = []
    search_url = f"https://www.google.com/search?q={stock_name}+news&tbm=nws"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    for item in soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd'):
        headline = item.get_text()
        if headline:
            headlines.append(headline)
        if len(headlines) >= 10:
            break
    
    return headlines

stocks = ["Tata Consultancy Services Limited", "Infosys Limited"]

for stock in stocks:
    print(f"Headlines for {stock}:")
    headlines = get_news_headlines(stock)
    for i, headline in enumerate(headlines, 1):
        print(f"{i}. {headline}")
    print("\n")