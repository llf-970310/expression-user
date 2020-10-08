import json

import requests


def get_sessionkey_openid(code: str, appid, secret):
    openid_url = 'https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&' \
                 'grant_type=authorization_code'.format(appid, secret, code)
    ret = json.loads(requests.get(openid_url).text)
    err_code = ret.get('errcode', 0)
    if err_code:
        return err_code, None, None
    session_key = ret.get('session_key')
    openid = ret.get('openid')
    return 0, session_key, openid
