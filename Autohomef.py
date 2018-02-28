from hashlib import md5
import requests
import re
import time
import ip_proxy
from random import randint,shuffle
class Autohome:
    def __init__(self,name,pswd):
        self.port =ip_proxy.get_prxiers1()
        self.headers={
            'Accept-Encoding':'gzip, deflate, br',
            'Host':'account.autohome.com.cn',
            'Referer':'https://account.autohome.com.cn/?backurl=https%3A%2F%2Fwww.autohome.com.cn%2Fshanghai%2F',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest',
            'Cookie':'sessionip=%s'%(re.findall('(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])',str(self.port))[0])
        }
        self.name=name
        self.pswd=self.pswd_md5(pswd)
        self.data={
            'name':self.name,
            'pwd':self.pswd,
            'validcode':'',
            'isauto':'false',
            'type':'json',
            'backurl':'https%3a%2f%2fwww.autohome.com.cn%2fshanghai%2f',
            'url':'https%3a%2f%2fwww.autohome.com.cn%2fshanghai%2f',
            'fPosition':0,
            'sPosition':0,
            'platform':1,
            'popWindow':0
        }
        self.sise = requests.session()
    def pswd_md5(self,pswd):
        smd5=md5()
        smd5.update(pswd.encode('UTF-8'))
        return smd5.hexdigest()
    def login(self,url):
        try:
            seq = self.sise.get('https://account.autohome.com.cn', headers=self.headers, proxies=self.port,timeout=10)
            logined=self.sise.post(url,headers=self.headers,data=self.data,proxies=self.port,timeout=10)
            # print(logined.text)
        except:
            return 'ipflass'
        return '登入成功'
    def reply(self,url,content):
        compgage=re.compile('tz.uniquePageId = "(.*?)"')
        headers = {
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        #print(self.sise.get(url,headers=headers).text)
        try:
            uniquepageid=compgage.findall(self.sise.get(url,headers=headers,proxies=self.port).text,re.S)
        except:
            return 'ipflass'
        bbsid=re.findall(r'https://club.autohome.com.cn/bbs/thread-c-(\d+)-\d+-\d+.html',url)[0]
        topicid=re.findall(r'https://club.autohome.com.cn/bbs/thread-c-\d+-(\d+)-\d+.html',url)[0]
        data={
                 'bbs':'c',
                 'bbsid': bbsid,
                 'topicId': topicid,
                 'content':content,
                 'uniquepageid':uniquepageid,#'64ysyB5EcuIAXvoQYcmpOco3FqqFEnFZBimcp5Pn06w=',
                'domain':'autohome.com.cn'
        }
        headers['Referer'] = url
        headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        try:
             req=self.sise.post('https://club.autohome.com.cn/Detail/AddReply',data=data,proxies=self.port,headers=headers,timeout=10)
             print(req.headers,req.cookies)
        except:
            return 'ipflass'
        print(req.text)
        if re.search('请先登录后再回复',req.text):
            return 'loginfalss'
        elif re.search('您由于违规被全论坛永久禁言',req.text):
            return '账号已经被封了'
        return '回复成功'
def get_name():
   with open('汽车之家.txt','r')as f:
       name=f.readlines()
   namelist=[]
   for i in name:
       if i == '\n':
           continue
       i = i.strip()  # 去除\n
       i = i.split('----')
       namelist.append(i)
   shuffle(namelist)
   print(namelist)
   return namelist
def get_conten():
    with open('内容.txt','r')as f :
        conten=f.readlines()
    return conten
def main(link):
    namelist=get_name()
    contenlist=get_conten()
    for i in namelist:
        while True:
            conten=contenlist[randint(0, len(contenlist) - 1)].strip()
            #print('账号:%s  密码%s: 回复内容%s:'%(i[0],i[1],conten))
            aut = Autohome(i[0],i[1])
            relogin=aut.login('https://account.autohome.com.cn/Login/ValidIndex')
            if relogin=='ipflass':
                time.sleep(5)
                continue
            rep = aut.reply(link,conten)
            print(rep)
            if rep=='ipflass':
                time.sleep(5)
                continue
            elif rep=='loginfalss':
                time.sleep(5)
                continue
            time.sleep(randint(20,50))
            yield i[0],rep
            break
    yield '','执行完毕'
if __name__ == '__main__':
    while True:
        link=input('输入链接:')
        if re.search('https://club.autohome.com.cn/bbs/thread-c-\d+-\d+-\d+.html',link):
            print('链接正确')
            main(link)
            break
        else:
            print('链接错误请重新输入')
