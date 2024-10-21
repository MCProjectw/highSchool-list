import requests
from bs4 import BeautifulSoup

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

html_content = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>뉴스 목록</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>뉴스: 고등학교</h1>
    <ul>
"""

for idx, title in enumerate(news_titles):
    news_title = title.get_text().strip()
    news_link = title['href']
    html_content += f'<li><a href="{news_link}">{news_title}</a></li>\n'

html_content += """
    </ul>
    <h2>딥페이크 관련 뉴스</h2>
    <ul>
"""

for idx, title in enumerate(deepfake_titles[:3]):
    news_title = title.get_text().strip()
    news_link = title['href']
    html_content += f'<li><a href="{news_link}">{news_title}</a></li>\n'

html_content += """
    </ul>
</body>
</html>
"""

with open('news_list.html', 'w', encoding='utf-8') as file:
    file.write(html_content)
