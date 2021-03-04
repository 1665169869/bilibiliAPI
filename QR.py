import requests
from time import time
from bilibiliAPI.sign import sign
# 二维码登录
# web端流程&逻辑：

# 获取二维码内容url以及密钥，以二维码内容url生成二维码，等待手机客户端扫描
# 以密钥作为参数进行POST
# if code == true goto 6 else goto 4（是否已经确认）
# if data == -4 goto 2 else goto 5（是否已经扫描）
# if data == -5 goto 3 & 提示已扫描 else goto 1&提示二维码超时或错误（密钥是否有效）
# 成功后会自动配置cookie 如需登录游戏分站则访问data.url中的url
# TV端流程&逻辑：

# 获取二维码内容url以及密钥，以二维码内容url生成二维码，等待手机客户端扫描
# 以密钥作为参数进行POST
# if code == 0 提示扫码成功并存储access_key于refersh_key else goto 4
# if code == 86039 提示未扫描&goto 2 else goto 5
# if code == 86038 提示二维码超时或错误&goto 1
class QR:
    def __init__(self):
        self.getLoginUrl = "http://passport.bilibili.com/qrcode/getLoginUrl"
        self.getLoginInfo = "http://passport.bilibili.com/qrcode/getLoginInfo"
        self.passportTvLogin = "http://passport.bilibili.com/x/passport-tv-login/qrcode/auth_code"
        self.passportTvLoginPoll = "http://passport.bilibili.com/x/passport-tv-login/qrcode/poll"
        self.appsec = "59b43e04ad6965f34319062b478f83dd"
        self.appkey = "4409e2ce8ffd12b8"
    def QRCodeLogin(self):
        '''
        申请二维码URL及扫码密钥（web端）
        参考：https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/login/login_action/QR.md#%E7%94%B3%E8%AF%B7%E4%BA%8C%E7%BB%B4%E7%A0%81url%E5%8F%8A%E6%89%AB%E7%A0%81%E5%AF%86%E9%92%A5web%E7%AB%AF
        请求方式：GET
        密钥超时为180秒
        '''
        response = requests.get(self.getLoginUrl)
        return response
    def scanCodeLogin(self, oauthKey, gourl="http://www.bilibili.com"):
        '''
        使用扫码登录（web端）
        参考：https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/login/login_action/QR.md#%E4%BD%BF%E7%94%A8%E6%89%AB%E7%A0%81%E7%99%BB%E5%BD%95web%E7%AB%AF
        请求方式：POST
        密钥超时为180秒
        验证登录成功后会进行设置以下cookie项：
        DedeUserID DedeUserID__ckMd5 SESSDATA bili_jct
        正文参数（ application/x-www-form-urlencoded ）：
        '''
        data = {
            "oauthkey": oauthKey,
            "gourl": gourl
        }
        response = requests.post(self.getLoginInfo, data=data)
        return response
    def QRCodeLoginTV(self):
        '''
        申请二维码URL及扫码密钥（TV端）
        参考：https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/login/login_action/QR.md#%E7%94%B3%E8%AF%B7%E4%BA%8C%E7%BB%B4%E7%A0%81url%E5%8F%8A%E6%89%AB%E7%A0%81%E5%AF%86%E9%92%A5tv%E7%AB%AF
        请求方式：POST
        鉴权方式：appkey
        密钥超时为180秒
        本接口可申请用于APP方式登录的access_key
        正文参数（ application/x-www-form-urlencoded ）：
        参数名	    类型	内容	    必要性	    备注
        appkey	    str	    APP密钥	    APP方式必要	仅可用4409e2ce8ffd12b8
        local_id	str	    TV端ID	    TV端必要	可为0
        ts	        num	    当前时间戳	APP方式必要	
        sign	    str	    APP签名	    APP方式必要	
        '''
        ts = int(time())
        # 只需要在ts后面加上sign盐值然后把表单md5加密即得到sign值
        data = {
            "appkey": self.appkey,
            "local_id": "0",
            "ts": ts,
            "sign": sign("appkey=4409e2ce8ffd12b8&local_id=0&ts=" + ts + self.appsec)
        }
        response = requests.post(self.passportTvLogin, data=data)
        return response
    def scanCodeLoginTV(self, auth_code):
        '''
        使用扫码登录（TV端）
        参考：https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/login/login_action/QR.md#%E4%BD%BF%E7%94%A8%E6%89%AB%E7%A0%81%E7%99%BB%E5%BD%95tv%E7%AB%AF
        请求方式：POST
        鉴权方式：appkey
        密钥超时为180秒
        验证登录成功后会返回可用于APP方式登录的access_key以及refresh_token
        '''
        ts = int(time())
        data = {
            "appkey": self.appkey,
            "auth_code": auth_code,
            "local_id": 0,
            "ts": ts,
            "sign":sign("appkey="+self.appkey+"&auth_code="+auth_code+"local_id=0&ts="+ts+self.appsec)
        }
        response = requests.post(self.passportTvLoginPoll,data=data)
        return response
