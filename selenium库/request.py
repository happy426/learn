import requests

web = requests.get('https://www.baidu.com')

print(web.text)


