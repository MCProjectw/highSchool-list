import feedparser

# RSS 피드 주소 (고등학생 관련 뉴스 검색)
rss_url = "https://news.google.com/rss/search?q=%EA%B3%A0%EB%93%B1%ED%95%99%EC%83%9D&hl=ko&gl=KR&ceid=KR:ko"

# 피드 데이터 가져오기
feed = feedparser.parse(rss_url)

# HTML 생성
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>이달의 고등학생 관련 뉴스</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>이달의 고등학생 관련 뉴스</h1>
    <ul>
"""

half_count = len(feed.entries) // 2
for entry in feed.entries[:half_count]:
    html_content += f"""
    <li>
        <h2><a href="{entry.link}" target="_blank">{entry.title}</a></h2>
    </li>
    """

html_content += """
    </ul>
</body>
</html>
"""

with open('news.html', 'w', encoding='utf-8') as file:
    file.write(html_content)
