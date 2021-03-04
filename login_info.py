import requests
from time import time
from bilibiliAPI.sign import sign

class login_info:
    # 统一返回response
    def __init__(self, access_key=""):
        self.NAVIGATION_BAR_USER_INFORMATION_ESCAPE = "http://api.bilibili.com/nav"
        self.NAVIGATION_BAR_USER_INFORMATION = "http://api.bilibili.com/x/web-interface/nav"
        self.LOGIN_USER_LNFORMATION = "http://app.bilibili.com/x/v2/account/myinfo"
        self.NUMBER_OF_LOGGED_IN_USER_STATUS = "http://api.bilibili.com/x/web-interface/nav/stat"
        self.GETCOIN = "http://account.bilibili.com/site/getCoin"
        self.APPKEY = "1d8b6e7d45233436"
        self.appsec = "560c52ccd288fed045859ed18bffd973"
        self.ACCESS_KEY = access_key
    def navigationBarUserInformation(self, SESSDATA, ifEscape=False):
        '''
        导航栏用户信息
        参考：https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/login/login_info.md#%E5%AF%BC%E8%88%AA%E6%A0%8F%E7%94%A8%E6%88%B7%E4%BF%A1%E6%81%AF
        NAVIGATION_BAR_USER_INFORMATION_ESCAPE ==           导航栏用户信息转义接口
        NAVIGATION_BAR_USER_INFORMATION        ==           导航栏用户信息接口
        SESSDATA                               ==           认证方式：仅可Cookie（SESSDATA）
        请求方式：GET
        参考：https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/login/login_info.md
        '''
        headers = {
            "cookie": "SESSDATA=" + SESSDATA,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81"
        }
        if ifEscape == True:
            response = requests.get(self.NAVIGATION_BAR_USER_INFORMATION_ESCAPE, headers=headers)
        else:
            response = requests.get(self.NAVIGATION_BAR_USER_INFORMATION, headers=headers)
        return response
    def loginUserLnformation(self):
        '''
        登录用户信息（APP端）
        参考：https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/login/login_info.md#%E7%99%BB%E5%BD%95%E7%94%A8%E6%88%B7%E4%BF%A1%E6%81%AFapp%E7%AB%AF
        请求方式：GET
        认证方式：仅可APP
        鉴权方式：appkey
        appkey                                  ==              APP密钥
        access_key                              ==              APP登录Token
        ts                                      ==              当前时间戳
        sign                                    ==              APP签名
        NUMBER_OF_LOGGED-IN_USER_STATUS         ==              登录用户状态数接口（双端）
        '''
        ts = int(time())
        params = {
            "access_key": self.ACCESS_KEY,
            "appkey": self.APPKEY,
            "ts": ts,
            "sign": sign("access_key=" + self.ACCESS_KEY + "&appkey=" + self.APPKEY + "&ts=" + ts + self.appsec)
        }
        response = requests.get(self.LOGIN_USER_LNFORMATION, params=params)
        return response
    def numberOfLoggedInUserStatus(self, SESSDATA=""):
        '''
        登录用户状态数（双端）
        参考：https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/login/login_info.md#%E7%99%BB%E5%BD%95%E7%94%A8%E6%88%B7%E7%8A%B6%E6%80%81%E6%95%B0%E5%8F%8C%E7%AB%AF
        请求方式：GET
        认证方式：Cookie（SESSDATA）或APP
        SESSDATA                ==           认证方式：仅可Cookie（SESSDATA）
        access_key              ==              APP登录Token
        '''
        headers = {
            "cookie": "SESSDATA=" + SESSDATA,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81"
        }
        if SESSDATA != "":
            response  = requests.get(self.NUMBER_OF_LOGGED_IN_USER_STATUS, headers=headers)
        else:
            response = requests.get(self.NUMBER_OF_LOGGED_IN_USER_STATUS, params={"access_key":self.ACCESS_KEY})
        return response
    def getCoin(self, SESSDATA):
        '''
        获取硬币数
        参考：https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/login/login_info.md#%E8%8E%B7%E5%8F%96%E7%A1%AC%E5%B8%81%E6%95%B0
        请求方式：GET
        认证方式：仅可Cookie（SESSDATA）
        '''
        headers = {
            "cookie": "SESSDATA=" + SESSDATA,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81"
        }
        response = requests.get(self.GETCOIN, headers=headers)
        return response