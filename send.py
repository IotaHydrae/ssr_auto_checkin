'''
POST https://kexue.ga/auth/send HTTP/1.1
Host: kexue.ga
Connection: keep-alive
Content-Length: 25
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: https://kexue.ga
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Referer: https://kexue.ga/auth/register
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: _ga=GA1.2.1108560974.1582044168; _gid=GA1.2.440994682.1582044168; ip=ff71a0e20f3dd31578f8c59231e7fc66; expire_in=1582648976; _gat=1

email=1144324368%40qq.com
'''
import requests

url='https://kexues.icu/auth/send'

data={
    'email': '2686755929@qq.com'
}

res = requests.post(url,data)
print(res.content.decode())