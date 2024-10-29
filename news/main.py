import requests
from bs4 import BeautifulSoup
import json

def fetch_news(keyword):
    url = f'https://search.naver.com/search.naver?where=news&query={keyword}'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('a', class_='news_tit')
    return titles

keyword1 = '고등학교'
keyword2 = '딥페이크'

news_titles = fetch_news(keyword1)
deepfake_titles = fetch_news(keyword2)

news_data = {
    "고등학교 관련 뉴스": [],
    "딥페이크 관련 뉴스": []
}

# 고등학교 관련 뉴스
for title in news_titles:
    news_title = title.get_text().strip()
    news_link = title['href']
    news_data["고등학교 관련 뉴스"].append({
        "title": news_title,
        "link": news_link
    })

# 딥페이크 관련 뉴스
for title in deepfake_titles[:5]:
    news_title = title.get_text().strip()
    news_link = title['href']
    news_data["딥페이크 관련 뉴스"].append({
        "title": news_title,
        "link": news_link
    })

with open('new.json', 'w', encoding='utf-8') as json_file:
    json.dump(news_data, json_file, ensure_ascii=False, indent=4)
