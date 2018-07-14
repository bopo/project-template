import requests
from django.conf import settings
from django.http import HttpResponse, JsonResponse

# from .libs.django_jwt_session_auth import jwt_login
# from .libs.WXBizDataCrypt import WXBizDataCrypt


def jscode2session(appkey, secret, js_code):
    base_url = 'https://api.weixin.qq.com/sns/jscode2session'
    params = {
        'appid': appkey,
        'secret': secret,
        'js_code': js_code,
        'grant_type': 'authorization_code',
    }

    response = requests.get(base_url, params=params)
    return response.json()


def login(request, *args, **kwargs):
    if request.method == 'POST':
        # iv = request.POST.get('iv', '')
        # encrypted_data = request.POST.get('encryptedData', '')

        # session_key = session_info['session_key']
        # open_id = session_info['openId']

        # crypt = WXBizDataCrypt(appid, session_key)
        # user_info = crypt.decrypt(encrypted_data, iv)

        # try:
        #     user = Person.objects.get(open_id=open_id)
        # except Person.DoesNotExist:
        #     user = register(user_info)

        # token = jwt_login(user, request)
        # user_info['token'] = 'token.decode()'

        # appkey = 'wx36c46674a4994557'
        # secret = 'dcd8f61d0d77596d6bdbd2957b9dfccf'

        appkey = settings.WEAPP_APPKEY
        secret = settings.WEAPP_SECRET

        code = request.POST.get('code', '')
        info = jscode2session(appkey, secret, code)
        # info = jwt_login(user, request)

        return JsonResponse(info)

    return HttpResponse('no code')
