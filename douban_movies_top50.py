import requests
from bs4 import BeautifulSoup
import time

# 获取单页电影数据
def get_movies_page(page):
    url = f'https://movie.douban.com/top250?start={(page-1)*25}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"请求第{page}页失败，状态码：", response.status_code)
        return None
    return BeautifulSoup(response.text, 'html.parser')

# 主函数
def main():
    all_movies = []
    
    # 获取前2页数据(共50条)
    for page in range(1, 3):
        soup = get_movies_page(page)
        if not soup:
            continue
            
        items = soup.find_all('div', class_='item')
        all_movies.extend(items)
        time.sleep(2)  # 防止请求过于频繁
    
    # 处理并输出电影数据
    print(f"开始获取数据，共找到{len(all_movies)}条电影信息")
    for index, item in enumerate(all_movies[:50]):
        title = item.find('span', class_='title').text
        rating = item.find('span', class_='rating_num').text
        link = item.find('a')['href']
        print(f"{index + 1}. 标题: {title}, 评分: {rating}, 链接: {link}")
    
    print(f"数据获取完成，共处理{len(all_movies)}条电影信息")

if __name__ == '__main__':
    main()