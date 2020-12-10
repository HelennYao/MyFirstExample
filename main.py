# %%
import requests
from bs4 import BeautifulSoup
import time
import random

# %%
# 模拟浏览器
# simul_header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
#     "Connection": "keep-alive",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#     "Accept-Language": "zh-CN,zh;q=0.8"}

# %%
# 遍历每一页
for i in range(1, 100):

    # 假装休眠
    my_sleep_0 = random.uniform(1,2)

    print('准备获取第' + str(i) + '页的图片，假装等待' + str(my_sleep_0) + '秒')
    time.sleep(my_sleep_0)
    print('假装完毕。')

    # 每一页的request的url
    top_dir = 'https://wallhaven.cc/search?categories=111&purity=110&atleast=1920x1080&ratios=16x9&topRange=1M&sorting=toplist&order=desc&page=' + str(
        i)

    # 将request到的结果赋值给r
    # r = requests.get(top_dir, headers=simul_header)
    r = requests.get(top_dir)
    # print(r.status_code)

    # 做碗汤
    soup = BeautifulSoup(r.text, features='lxml')
    # 解析html内容
    urls = soup.find_all('a', class_='preview', target='_blank')
    # 在具体某一页遍历所有的图片
    for item in range(0, len(urls)):
        # 记得休眠
        my_sleep_1 = random.uniform(1,2)
        print(
            '正准备获取第' + str(i) + '页的第' + str(item + 1) + '张图片，一共有' + str(len(urls)) + '张图片。假装等待' + str(my_sleep_1) + '秒')
        time.sleep(my_sleep_1)
        print('假装完毕。')

        # 解析html内容
        html_dir = urls[item].get('href')
        # r_1 = requests.get(html_dir, headers=simul_header)
        r_1 = requests.get(html_dir)
        soup_1 = BeautifulSoup(r_1.text, features='lxml')

        ph = soup_1.find_all('img', id="wallpaper")
        # 保存图片
        for img in ph:
            link = img.get('src')
            print('正在下载图片...')
            response1 = requests.get(link)
            print('下载完毕，正在保存...')
            with open('./saved_ph/' + str(i) + '_' + str(item + 1) + '.jpg', 'wb') as file:
                file.write(response1.content)
            print('保存完毕！')
