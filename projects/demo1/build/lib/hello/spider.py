import requests


def fetch():
    response = requests.get('http://www.baidu.com')
    print(response)
    return response
