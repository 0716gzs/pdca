"""
生成微信小程序二维码

"""
import requests
import json
from PIL import Image
from io import BytesIO
from django.conf import settings
import os


base_url = "https://api.weixin.qq.com"


def cgi_bin_token(appid, secret, grant_type, flag=False):
    res = requests.get(f'{base_url}/cgi-bin/token?grant_type={grant_type}&appid={appid}&secret={secret}')
    if flag is False:
        return json.loads(res.text)
    else:
        result = res.json()
        if 'access_token' in result:
            return result['access_token']
        else:
            raise Exception(f"Error: {result.get('errmsg', 'Unknown error')}")


# 获取二维码
def get_qrcode_wx_url():
    from urllib.parse import urlencode
    url = 'https://open.weixin.qq.com/connect/oauth2/authorize?' + urlencode({
        'appid': settings.CORP_ID,
        'redirect_uri': settings.REDIRECT_URI,
        'response_type': 'code',
        'scope': settings.SCOPE,
        'state': settings.STATE
    }) + '#wechat_redirect'

    return url


def createwxaqrcode(appid, secret, grant_type, path):
    token = cgi_bin_token(appid, secret, grant_type)
    data = {
        "path": path,
        "width": 430
    }
    respone = requests.post(f'{base_url}/cgi-bin/wxaapp/createwxaqrcode?access_token={token["access_token"]}', data=json.dumps(data))

    content = respone.content
    if not content:
        return '没有二进制流'

    # img = Image.open(BytesIO(content))
    #
    # file = f"{settings.STATICFILES_DIRS[0]}/public/miniprog.png"
    # if not os.path.exists(file):
    #     img.save(file)
    return content
