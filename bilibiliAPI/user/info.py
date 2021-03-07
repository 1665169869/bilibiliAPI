import requests

def spaceInfo(mid, SESSDATA=""):
    API = "http://api.bilibili.com/x/space/acc/info" 
    #参考：https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/user/info.md#%E7%94%A8%E6%88%B7%E8%AF%A6%E7%BB%86%E4%BF%A1%E6%81%AF1-%E7%94%A8%E4%BA%8E%E7%A9%BA%E9%97%B4
    #用户详细信息1 (用于空间)
    params = {
        "mid": mid
    }
    headers = {
        "cookies": "SESSDATA="+SESSDATA
    }
    return requests.get(API, params=params, headers=headers)

def userDetailsCards(mid, SESSDATA="", photo=False):
    API = "http://api.bilibili.com/x/web-interface/card" 
    #参考：https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/user/info.md#%E7%94%A8%E6%88%B7%E8%AF%A6%E7%BB%86%E4%BF%A1%E6%81%AF2-%E7%94%A8%E4%BA%8E%E5%90%8D%E7%89%87
    #用户详细信息2 (用于名片)
    params = {
        "mid": mid,
        "photo": photo
    }
    headers = {
        "cookies": "SESSDATA="+SESSDATA
    }
    return requests.get(API, params=params, headers=headers)

def spaceMyInfo(SESSDATA):
    # 本用户详细信息
    # https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/user/info.md#%E6%9C%AC%E7%94%A8%E6%88%B7%E8%AF%A6%E7%BB%86%E4%BF%A1%E6%81%AF
    API = "http://api.bilibili.com/x/space/myinfo"
    headers = {
        "cookies": "SESSDATA="+SESSDATA
    }
    return requests.get(API, headers=headers)
