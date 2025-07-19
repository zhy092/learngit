import requests
from bs4 import BeautifulSoup
import json

url = 'https://movie.douban.com/top250'
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    movies = []
    
    for item in soup.select('.item'):
        title = item.select_one('.title').text.strip()
        rating = item.select_one('.rating_num').text.strip()
        movies.append({'title': title, 'rating': rating})
    
    with open('douai_top250.json', 'w', encoding='utf-8') as f:
        json.dump(movies, f, ensure_ascii=False, indent=2)
        
    print("成功抓取{}条数据".format(len(movies)))
except Exception as e:
    print("抓取失败:", e)
