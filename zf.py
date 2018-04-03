#! usr/bin/python
# coding:utf-8

import requests
from bs4 import BeautifulSoup
s=requests.Session()
code_url="http://210.38.137.126:8016/CheckCode.aspx"
headers={
    "Host":"210.38.137.126:8016",
    "Referer":"http://210.38.137.126:8016/default2.aspx",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "__VIEWSTATE":"dDwxNTMxMDk5Mzc0Ozs+OBE730NQqeUlEYO76T3Qls4CiUo=",
    }
r=s.get(code_url,headers=headers)
with open("./aaaaaa.jpg","wb") as img:
    img.write(r.content)
login_url="http://210.38.137.126:8016/default2.aspx"
login_headers={
    "Host": "210.38.137.126:8016",
    "Origin": "http://210.38.137.126:8016",
    "Upgrade-Insecure-Requests": "1",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Referer": "http://210.38.137.126:8016/default2.aspx"
    }
code=raw_input("please input v_code:\n")
data={
    "__VIEWSTATE":"dDwxNTMxMDk5Mzc0Ozs+OBE730NQqeUlEYO76T3Qls4CiUo=",
    "txtUserName":"201412911420",
    "TextBox2":"19951219abc",
    "txtSecretCode": code,
    "Button1":"",
    "Textbox1":""
    }

res=s.post(login_url,headers=login_headers,data=data)
print("登录成功")
refer="http://210.38.137.126:8016/xs_main.aspx?xh=201412911420"
kburl="http://210.38.137.126:8016/xskbcx.aspx?xh=201412911420&xm=%C2%AC%CB%BC%CE%B0&gnmkdm=N121602"
kb_headers={
        "Referer":refer,
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }
kb_res=s.get(kburl,headers=kb_headers)
soup=BeautifulSoup(kb_res.text,"lxml")
kb=soup.find(id="Table1")
kb_text=kb.get_text()

print(kb_text)
