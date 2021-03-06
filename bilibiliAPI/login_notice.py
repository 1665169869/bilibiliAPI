from requests import get
def login_notice(mid="",SESSDATA="",buvid="",proxies={}):
    '''
    登录记录
    参考：https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/login/login_notice.md
    参数名	类型	内容	必要性	备注
    mid	num	用户UID	必要	
    buvid	str	    设备ID	非必要	为操作登录接口时Cookie中的buvid3可为任意值
    '''
    headers = {
        "cookie": "SESSDATA=" + SESSDATA,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81"
    }
    params = {
        "mid": mid,
        "buvid": buvid
    }
    return get("http://api.bilibili.com/x/safecenter/login_notice", headers=headers, proxies=proxies, params=params)

