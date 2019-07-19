
import requests
#设置session可以自动保存cookies，可设置请求参数，下次请求自动带上请求参数


s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)

s = requests.Session()
s.auth = ('user','pass')#权限认证
s.headers.update({'x-test':'true'})
print(s.headers)