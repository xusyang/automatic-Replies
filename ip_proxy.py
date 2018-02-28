import requests
import json
import Autohomef
import time
def  get_prxiers():
    url='http://tvp.daxiangdaili.com/ip/'
    data={
    'tid':'555888625928201',
    'num':1,
    'operator':1,
    'filter':'on',
    'category':2,
    'protocol':'https',
    'sortby':'time',
    'delay':1,
    'format':'json',
    }
    jsons=requests.get(url,params=data).text
    jsons=json.loads(jsons)
    ip=jsons[0]['host']
    port=jsons[0]['port']
    proxies = { "http": "http://%s:%s"%(ip,port), "https": "http://%s:%s"%(ip,port),}
    seq=requests.get('https://club.autohome.com.cn/bbs/forum-c-3899-2.html?qaType=-1#pvareaid=101061',timeout=3)
    print(seq)
    time.sleep(2)
    if seq.status_code==200:
        print(proxies)
        return proxies
    else:
        return get_prxiers()
def get_prxiers1():
    req=requests.get('http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=c1248b997f1e400baa588162225c9c6c&orderno=YZ201711144064pRUpC5&returnType=2&count=1')
    req=json.loads(req.text)
    try:
        prot={
            'https': 'http://%s:%s'%(req['RESULT'][0]['ip'],req['RESULT'][0]['port']) ,'http': 'http://%s:%s'%(req['RESULT'][0]['ip'],req['RESULT'][0]['port'])
            }
    except:
        prot=None
    return prot
if __name__ == '__main__':
    headers={
    'Referer':'http://www.ip138.com/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
        }
    ipotr=get_prxiers1()
    req=requests.get('http://2017.ip138.com/ic.asp',headers=headers,proxies=ipotr)
    print(req.content.decode('gbk'))
#     while 10000:
#         try:
#             prip = get_prxiers()
#             Aut = Autohomef.Autohome('13524873489', 'WANGJING130', prip)
#             re=Aut.login('https://account.autohome.com.cn/Login/ValidIndex')
#             f = open('ip.txt', 'a')
#             f.write(str(prip) + '\n')
#             f.close()
#             print(len(re))
#         except:
#             continue

