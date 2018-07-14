from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from wechatpy import WeChatOAuth, WeChatOAuthException

from .. import WeiMsg, check_signature
from ..handlers import default_handler, router_patterns
from ..routers import base_router, db_router

routers = [base_router, db_router]


@csrf_exempt
def gateway(request, *args, **kwargs):
    if request.method == 'GET':
        if check_signature(request, settings.WECHAT_TOKEN):
            return HttpResponse(request.GET.get('echostr'))

        return HttpResponse('不提供直接访问！')

    if request.method == 'POST':
        recv_msg = WeiMsg(request.body.decode())

        for router in routers:
            result = router(recv_msg, router_patterns)

            if isinstance(result, HttpResponse):
                return result

        return default_handler(recv_msg)


def authorize(func, *args, **kwargs):
    '''
    认证接口
    :param request:
    :return:
    '''

    def returned_wrapper(request, *args, **kwargs):
        try:
            user = request.session.get('user', None)

            if user is None:
                code = request.GET.get('code', None)

                auth = WeChatOAuth(settings.WECHAT_APPKEY, settings.WECHAT_SECRET,
                                   redirect_uri=request.build_absolute_uri(request.get_full_path()))

                if code is None:
                    return HttpResponseRedirect(auth.authorize_url)

                access = auth.fetch_access_token(code)
                # auth.refresh_access_token(access.get('refresh_token'))
                userinfo = auth.get_user_info()

                request.session['user'] = userinfo
                request.session['access'] = access
                request.session.set_expiry(int(access.get('expires_in')))
        except WeChatOAuthException as e:
            # raise e
            auth = WeChatOAuth(settings.WECHAT_APPKEY, settings.WECHAT_SECRET,
                               redirect_uri=request.build_absolute_uri(request.get_full_path()))
            return HttpResponseRedirect(auth.authorize_url)

        return func(request, *args, **kwargs)

    return returned_wrapper


@authorize
def userinfo(request, *args, **kwargs):
    return JsonResponse(request.session['user'])
