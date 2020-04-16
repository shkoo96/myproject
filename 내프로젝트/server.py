from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
import urllib
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db= client.dbsparta

def run_server():
    server = Flask('주문서버')

    @server.route('/')
    def home():
        return render_template("index.html")

    @server.route('/info', methods=['POST'])
    def write_weather():
        location_receive = request.form['location_give']
        enc_location = urllib.parse.quote(location_receive + '+날씨')
        url = 'https://search.naver.com/search.naver?query=' + enc_location

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
        data = requests.get(url, headers=headers)

        soup = BeautifulSoup(data.text, 'html.parser')

        info = soup.select('div.info_data')[0]
        temp_now = info.select_one('span.todaytemp').text.strip()
        min_temp = info.select_one('span.min').text.strip()
        max_temp = info.select_one('span.max').text.strip()
        sensible_temp = info.select_one('span.sensible > em').text.strip()

        weather = {
            'location' : location_receive,
            'temp_now' : temp_now,
            'min_temp' : min_temp,
            'max_temp' : max_temp,
            'sensible_temp' : sensible_temp
        }

        # 옷차림 찾기
        clothes = { 'type' : "반팔" }

        return jsonify({'result' : 'success', 'weather': weather, 'clothes': clothes})




    server.run('0.0.0.0', port=5000, debug=True)


run_server()