from django.http import JsonResponse
from wechatpy.pay import WeChatPay

from .mps import authorize


@authorize
def payment(request, *args, **kwargs):
    '''
    支付接口

    :param request:
    :return:
    '''
    # pass

    client = WeChatPay(appid='', api_key='', mch_id='', sub_mch_id=None,
                       mch_cert=None, mch_key=None, timeout=None, sandbox=False)

    client.jsapi.get_jsapi_params(prepay_id='', timestamp=None, nonce_str=None, jssdk=False)
    client.jsapi.get_jsapi_signature(prepay_id='', timestamp=None, nonce_str=None)

    return JsonResponse({'a': 'a'})
