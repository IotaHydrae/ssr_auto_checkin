'''
POST https://kexues.icu/auth/login HTTP/1.1
Host: kexues.icu
Connection: keep-alive
Content-Length: 63
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: https://kexues.icu
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Referer: https://kexues.icu/auth/login
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: _ga=GA1.2.1108560974.1582044168; _gid=GA1.2.440994682.1582044168; _gat=1

email=1657802074%40qq.com&passwd=2231841&code=&remember_me=week
'''
import requests
from header2dict import  header2dict
from bs4 import BeautifulSoup
url = "https://kexues.icu/auth/login"
header = '''Host: kexues.icu
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0
    Accept: application/json, text/javascript, */*; q=0.01
    Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
    Accept-Encoding: gzip, deflate, br
    X-Requested-With: XMLHttpRequest
    Origin: https://kexues.icu
    Connection: keep-alive
    Referer: https://kexues.icu/user
    Cookie: _ga=GA1.2.711495693.1580472729; _gid=GA1.2.615565355.1582277312; uid=1340; email=1657802074%40qq.com; key=7d5c895664ee210ade1837f973b78dd246832a8d6de0b; ip=cc6600ab77608f3c585450cab8d0fd5f; expire_in=1582882112; _gat=1
    Content-Length: 0
    TE: Trailers'''

header = '''Host: kexues.icu
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Cookie: __cfduid=def8b6f2800a43426efa793191cde1a331593923282; _ga=GA1.2.1043729039.1593923320; _gid=GA1.2.1716385751.1593923320; uid=1340; email=1657802074%40qq.com; key=b34849e316a137040b0e4c1514593d51f364a866b017e; ip=827d5c58c636680e5e48c6b409bc7d87; expire_in=1594528128
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0'''

header = header2dict(header)
data = {
    'email': '1657802074@qq.com',
    'passwd': '2231841',
    'code':'',
    'remeber_me': 'week'
}
# data = {
#     'email': '1144324368@qq.com',
#     'passwd': '2231841.',
#     'code':'',
#     'remeber_me': 'week'
# }

session = requests.session()
print('正在登陆。。。')
res = session.post(url,data,header)
login_status = res.status_code
if login_status == 200:
    print('已访问到登录页面')
login_result = res.json()
if login_result['ret'] == 1:
    print(login_result['msg'])



checkin_url = 'https://kexues.icu/user/checkin'
print('正在签到。。。')
res2 = session.post(checkin_url)
checkin_status = res2.status_code
if checkin_status == 200:
    checkin_result = res2.json()
    print(checkin_result['msg'])

user_url = 'https://kexues.icu/user'
print('转到用户中心页面')
res2 = session.get(user_url)
user_status = res2.status_code
if user_status == 200:
    soup = BeautifulSoup(res2.text, 'html.parser')
    div = soup.find(name='code', class_='card-tag tag-green')
    print("流量剩余: "+div.text)
