import requests
from bs4 import BeautifulSoup

def crawl_drawings_and_text():
    url = "https://arca.live/b/zzum"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for post in soup.select(".post-item"):
        img_url = post.select_one("img")["src"]
        description = post.select_one(".description").text
        with open("dataset.txt", "a", encoding="utf-8") as f:
            f.write(f"{img_url}\t{description}\n")

if __name__ == "__main__":
    crawl_drawings_and_text()
