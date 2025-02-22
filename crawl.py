import requests
from bs4 import BeautifulSoup
import time

BASE_URL = "https://arca.live"
BOARD_URL = f"{BASE_URL}/b/zzum"

def get_post_links():
    """게시판에서 게시글 링크 수집"""
    response = requests.get(BOARD_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    
    for post in soup.select(".vrow .title > a"):
        link = post["href"]
        if link.startswith("/b/zzum/"):  # 올바른 게시글 링크인지 확인
            links.append(BASE_URL + link)
    
    return links

def scrape_post(post_url):
    """게시글에서 이미지와 캡션 추출"""
    response = requests.get(post_url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    title = soup.select_one(".title").text.strip()
    images = [img["src"] for img in soup.select(".article img") if img.get("src")]
    
    return {"title": title, "images": images}

def crawl_drawings_and_text():
    """전체 크롤링 실행"""
    post_links = get_post_links()
    
    with open("dataset.txt", "a", encoding="utf-8") as f:
        for post_url in post_links:
            try:
                data = scrape_post(post_url)
                for img_url in data["images"]:
                    f.write(f"{img_url}\t{data['title']}\n")
                time.sleep(1)  # 서버 부담 방지를 위한 대기
            except Exception as e:
                print(f"Error scraping {post_url}: {e}")

if __name__ == "__main__":
    crawl_drawings_and_text()
