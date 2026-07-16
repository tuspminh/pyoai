import requests
import re
from bs4 import BeautifulSoup
import random
from time import sleep

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

URL = "https://www.zhenhunxiaoshuo.com/modu/"

response = requests.get(URL, headers=HEADERS, timeout=10)

soup = BeautifulSoup(response.content, "html.parser")

nodes = soup.select("article.excerpt.excerpt-c3 a")

# chapter = {}
chapters = []
count = 0
for node in nodes:
    title = node.get_text(strip=True)
    link = node.get("href")
    chapter_no = re.findall(r"\d+", title)
    if chapter_no:
        continue
        # title = f"Chapter-{chapter_no[0]}"
        # chapters.append({"title": title, "link": link})
        # print(f"Title: {title}, Link: {link}")
        # continue
    print(f"Ngoai_truyen_{count}, Link: {link}")
    chapters.append({"title": f"Ngoai_truyen_{count}", "link": link})
    count += 1


for chapter in chapters:
    # break
    print(f"crawling Chapter Title: {chapter['title']}, Link: {chapter['link']}")
    response = requests.get(chapter["link"], headers=HEADERS, timeout=10)
    soup = BeautifulSoup(response.content, "html.parser")
    content_node = soup.select_one("article.article-content")
    for a_tag in content_node.find_all("a", class_="google-anno"):
        a_tag.decompose()  # Xóa sạch sẽ thẻ và nội dung bên trong nó
    # print(f"Content: {content_node.get_text(strip=True, separator='\n\n')}")

    content = content_node.get_text(strip=True, separator="\n\n")

    if not content:
        # print(f"Warning: No content found for chapter {chapter['title']}")
        continue
    chapter_filename = f"{chapter['title']}.txt"
    with open(chapter_filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved chapter {chapter['title']} to {chapter_filename}")
    sleep(random.uniform(1, 3))  # Thêm độ trễ giữa các yêu cầu để tránh bị chặn IP
    # break
