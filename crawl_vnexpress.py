import requests
from bs4 import BeautifulSoup
import csv

def crawl_vnexpress():
    url = "https://vnexpress.net/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Lấy các bài viết từ mục "Mới nhất"
    articles = soup.select('.section_topstory .item-news')
    data = []
    for article in articles:
        title = article.select_one('h2.title-news a')
        if title:
            title_text = title.text.strip()
            link = title.get('href')
            data.append({'title': title_text, 'link': link})

    # Lưu dữ liệu vào file CSV
    with open('vnexpress_articles.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)

    print("Crawl completed! Data saved to vnexpress_articles.csv")

if __name__ == "__main__":
    crawl_vnexpress() 