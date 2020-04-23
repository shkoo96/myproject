from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
import urllib
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db= client.dbsparta



def run_server():
    server = Flask('기온별 옷차림 서버')

    @server.route('/')
    def home():
        return render_template("index.html")

    @server.route('/info', methods=['POST'])
    def write_weather():
        try:
            location_receive = request.form['location_give']
            enc_location = urllib.parse.quote(location_receive + '+날씨')
            url = 'https://search.naver.com/search.naver?query=' + enc_location

            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
            data = requests.get(url, headers=headers)

            soup = BeautifulSoup(data.text, 'html.parser')

            location = soup.select_one('div.lst_select').text.strip()
            info = soup.select('div.info_data')[0]
            temp_now = info.select_one('span.todaytemp').text.strip()
            weather_info = info.select_one('p.cast_txt').text.strip()
            min_temp = info.select_one('span.min').text.strip()
            max_temp = info.select_one('span.max').text.strip()
            sensible_temp = info.select_one('span.sensible > em').text.strip()

            weather = {
                'location' : location,
                'weather_info' : weather_info,
                'temp_now' : temp_now,
                'min_temp' : min_temp,
                'max_temp' : max_temp,
                'sensible_temp' : sensible_temp
            }

            temp = int(temp_now)
            clothes = []


            contents = list(db.clothes.find({},{'_id':0}))
            for content in contents:
                line = []
                max = int(content['max'])
                min = int(content['min'])
                if min <= temp and temp < max:
                    clothes.append(content)
            return jsonify({'result': 'success', 'weather': weather, 'clothes': clothes})
        except:
            return jsonify({'result':'fail', 'alert': '잘못된 위치입니다!'})

        # clothes = list(db.clothes.find({'$and' :[{'max': {'$gt': temp}}, {'min': {'$lte': temp}}]}, {'_id': 0}))
        # print(clothes)

        # return jsonify({'result' : 'success', 'weather': weather, 'clothes': clothes})


    @server.route('/admin')
    def admin():
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

        if db.clothes.find_one({'url': url}) is not None:
            return jsonify({'result': 'fail', 'msg': '이미 있는 옷입니다!'})

        html = urllib.request.urlopen(url).read()

        soup = BeautifulSoup(html, 'html.parser')
        info = soup.find("div", class_="keyImg")
        imgUrl = info.find("img")['src']
        imgName = info.find("img")['alt']

        cloth = {'max': max, 'min': min, 'type': type, 'mall': mall, 'url': url, 'imgUrl': imgUrl, 'imgName': imgName}
        db.clothes.insert_one(cloth)
        return jsonify({'result': 'success', 'msg': '옷 저장 성공!'})

        # result = {'max': max, 'min': min, 'type': type, 'mall': mall, 'url': url, 'imgUrl': imgUrl, 'img': img}
        # return result

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

    @server.route('/clothes', methods=['GET'])
    def read_clothes_list():
        clothes = list(db.clothes.find({}, {'_id': 0}))
        return jsonify({'result': 'success', 'clothes': clothes})

    @server.route('/admin/delete', methods=['POST'])
    def delete():
        url_receive =request.form['url_give']
        db.clothes.delete_one({'url': url_receive})
        return jsonify({'result': 'success', 'msg': 'Deleted Successfully!'})




    server.run('0.0.0.0', port=5000, debug=True)


run_server()