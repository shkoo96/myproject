import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

def insert_all():
    db.myclothes.drop() #myclothes 콜렉션을 모두 지워줌

    data1 = {
        'min': 28, 'max': " ",
        'clothes': [
            {
                'type': "민소매",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "반바지",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "반팔티",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            }
        ]
    }
    db.myclothes.insert_one(data1)

    data2 = {
        'min': 23, 'max': 27,
        'clothes': [
            {
                'type': "반팔티",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "반바지",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "치마",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            }
        ]
    }
    db.myclothes.insert_one(data2)


    data3 = {
        'min': 20, 'max': 22,
        'clothes': [
            {
                'type': "원피스",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "블라우스",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "긴팔티",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            }
        ]
    }
    db.myclothes.insert_one(data3)

    data4 = {
        'min': 17, 'max': 19,
        'clothes': [
            {
                'type': "가디건",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "긴바지",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "얇은니트",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            }
        ]
    }
    db.myclothes.insert_one(data4)

    data5 = {
        'min': 12, 'max': 16,
        'clothes': [
            {
                'type': "자켓",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "니트",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "기모치마",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            }
        ]
    }
    db.myclothes.insert_one(data5)

    data6 = {
        'min': 9, 'max': 11,
        'clothes': [
            {
                'type': "트렌치코트",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "야상",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "기모바지",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            }
        ]
    }
    db.myclothes.insert_one(data6)

    data7 = {
        'min': 5, 'max': 8,
        'clothes': [
            {
                'type': "울코트",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "히트텍",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "가죽옷",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            }
        ]
    }
    db.myclothes.insert_one(data7)

    data8 = {
        'min': " ", 'max': 4,
        'clothes': [
            {
                'type': "패딩",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "코트",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "목도리/장갑",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            }
        ]
    }
    db.myclothes.insert_one(data8)


