import time
import random
import requests
import pandas as pd
from bs4 import BeautifulSoup

def google_search(input_keyword_def,page_def):

    article_list = []
    check_list = []

    # 設定使用瀏覽器
    USER_AGENT = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        }

    for keyword in input_keyword_def:
        for page_number in range(page_def):
            
            # 爬取url的頁面設定
            page = str(0 + (10 * (page_number - 1)))
            url = f"https://www.google.com.tw/search?q={keyword}&start={page}"

            print(f"爬取關鍵字：{str(keyword)}, 第{str(page_number + 1)}頁")
            time.sleep(random.randrange(0, 2))
            
            res = requests.get(url, headers=USER_AGENT)
            soup = BeautifulSoup(res.text, "html.parser")
            search_list = soup.find(id="search").find_all(class_="g")

            for article in search_list:
                title = article.find("h3").text
                url = article.find("div").find("a").get("href")
                content = article.find(class_="aCOpRe").text
                if title not in check_list:
                    check_list.append(title)
                    article_list.append({
                        "tag": keyword,
                        "title": title,
                        "url": url,
                        "content": content
                    })
                else:
                    print("重複")


    df = pd.DataFrame(article_list)
    df.to_csv('~/Desktop/Result.csv', index=False)
    print("Done! 檔案已存入桌面")

def main():
    
    # 設定輸入關鍵字
    input_keyword = ["廣告投放","關鍵字廣告"]
    # 設定爬取頁數
    page = 3
    google_search(input_keyword,page)

if __name__ == '__main__':
    main()
