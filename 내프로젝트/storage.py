from flask import Flask, render_template, request
from pymongo import MongoClient
import requests
import urllib.request
from bs4 import BeautifulSoup

# url = 'http://906studio.co.kr/product/detail.html?product_no=2276'
# req = urllib.request.Request(url)
# html = urllib.request.urlopen(url).read()
#
# soup = BeautifulSoup(html, 'html.parser')
# info = soup.find("div", class_="keyImg")
# imgUrl = info.find("img")['src']
# img = info.find("img")['alt']
# print(imgUrl, img)

def start_server():
    server = Flask("옷 저장소")

    @server.route('/')
    def home():
        return render_template('storage.html')

    @server.route('/clothes', methods=['POST'])
    def add_clothes():
        max = request.form['max']
        min = request.form['min']
        type = request.form['type']
        mall = request.form['mall']
        url = request.form['url']
        # if max is None or min is None or type is None or mall is None or url is None:
        #     result = {'message': 'parameter not filled!', 'result': 'error'}
        #     return result


        html = urllib.request.urlopen(url).read()

        soup = BeautifulSoup(html, 'html.parser')
        info = soup.find("div", class_="keyImg")
        imgUrl = info.find("img")['src']
        img = info.find("img")['alt']
        result = {'max': max, 'min': min, 'type': type, 'mall': mall, 'url': url, 'imgUrl': imgUrl, 'img': img}
        return result

        # soup = BeautifulSoup(html, 'html.parser')
        # # metatag 찾아서 name, img, url 가져오기
        # # img : 906, 스타일난다, BLACKUP, Look at Min의 경우 div.keyImg > img src
        # # name : 906, 스타일난다, BLACKUP, Look at Min의 경우 div.keyImg > img alt
        # info = soup.find('div', class_="keyImg")
        # img = info.find("img")["src"]
        # # img = info.get("src")
        # # name = info.get("alt")
        #
        # print(img)

    server.run('0.0.0.0', port=5000, debug=True)


start_server()
