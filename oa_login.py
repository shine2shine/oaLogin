import requests

from bs4 import BeautifulSoup as bs


'''
本机IP: 125.120.32.219浙江省杭州市 电信 

   请求 URL: http://oa.tofine.com:8888/login/VerifyLogin.jsp
   
   Accept: text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8
   Accept-Encoding: gzip, deflate
   Accept-Language: en-US, en; q=0.8, zh-Hans-CN; q=0.5, zh-Hans; q=0.3
   Cache-Control: max-age=0
   Connection: Keep-Alive
   Content-Length: 310
   Content-Type: application/x-www-form-urlencoded
   Cookie: ecology_JSessionId=abcBCucho4nbMdP9KZkcx; testBanCookie=test
   Host: oa.tofine.com:8888
   Referer: http://oa.tofine.com:8888/wui/theme/ecology8/page/login.jsp?templateId=4&logintype=1&gopage=&languageid=7&message=17
   Upgrade-Insecure-Requests: 1
   User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362



   appid: 
   fontName: 微软雅黑
   formmethod: post
   gopage: 
   isie: false
   islanguid: 7
   loginfile: /wui/theme/ecology8/page/login.jsp?templateId=4&logintype=1&gopage=
   loginid: 00001
   logintype: 1
   message: 17
   rnd: 
   serial: 
   tokenAuthKey: 
   username: 
   userpassword: 00001
   weaverssoservice: 
   '''




header = {
   'Accept': 'text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8',
   'Accept-Encoding': 'gzip, deflate',
   'Accept-Language': 'en-US, en; q=0.8, zh-Hans-CN; q=0.5, zh-Hans; q=0.3',
   'Cache-Control': 'max-age=0',
   'Connection': 'Keep-Alive',
   'Content-Length': '310',
   'Content-Type': 'application/x-www-form-urlencoded',
   'Cookie': 'ecology_JSessionId=abcBCucho4nbMdP9KZkcx; testBanCookie=test',
   'Host': 'oa.tofine.com:8888',
   'Referer': 'http://oa.tofine.com:8888/wui/theme/ecology8/page/login.jsp?templateId=4&logintype=1&gopage=&languageid=7&message=17',
   'Upgrade-Insecure-Requests': '1',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'
   }

session = requests.session()

url = 'http://oa.tofine.com:8888'

r = session.get(url,headers = header)
# print(r.cookies)

loginurl = 'http://oa.tofine.com:8888/login/VerifyLogin.jsp'
postData = {
          'appid:':'',
   'fontName': '微软雅黑',
   'formmethod': 'post',
   'gopage': '',
   'isie': 'false',
   'islanguid': '7',
   'loginfile': '/wui/theme/ecology8/page/login.jsp?templateId=4&logintype=1&gopage=',
   'loginid': '00151',
   'logintype': '1',
   'message': '17',
   'rnd': '',
   'serial': '',
   'tokenAuthKey': '',
   'username': '',
   'userpassword': '33223',
   'weaverssoservice': ''
   }
        
rs = session.post(loginurl,data = postData,headers = header,cookies  = r.cookies)
print(len(rs.text))
# print(rs.text)
# rs.encoding = 'utf8'
# with open('login.txt' ,'w') as f:
#         f.write(rs.text)