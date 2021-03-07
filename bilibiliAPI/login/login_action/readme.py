import requests

# 参考：https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/login/login_action/readme.md

def RequestCAPTCHA():
    CAPTCHA_API = "http://passport.bilibili.com/web/captcha/combine?plat=6"
    # 未完工