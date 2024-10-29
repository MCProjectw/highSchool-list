import feedparser
import json

rss_url = "https://news.google.com/rss/search?q=%EA%B3%A0%EB%93%B1%ED%95%99%EC%83%9D&hl=ko&gl=KR&ceid=KR:ko"

# 피드 데이터 가져오기
feed = feedparser.parse(rss_url)

# JSON 구조 생성
news_data = {"고등학생 관련 뉴스": []}
half_count = len(feed.entries) // 2

for entry in feed.entries[:half_count]:
    news_item = {
        "title": entry.title,
        "link": entry.link
    }
    news_data["고등학생 관련 뉴스"].append(news_item)

# JSON 파일로 저장
with open('idal-news.json', 'w', encoding='utf-8') as file:
    json.dump(news_data, file, ensure_ascii=False, indent=4)
