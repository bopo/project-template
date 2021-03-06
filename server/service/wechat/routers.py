import re

from .models import PatternE2PT, PatternE2T, PatternT2PT, PatternT2T
from .utils import PTItem, pic_text_response, text_response


# ---------------- 参考 -----------------
# 参考信息：
# 消息类型：text, event, image, video, link , location,
def base_router(recv_msg, router_patterns):
    for type, key, handler in router_patterns:
        if recv_msg.msg_type == 'text':
            match = re.search(key, recv_msg.content)
            if match:
                return handler(recv_msg, router_patterns)
        elif recv_msg.msg_type == type:
            return handler(recv_msg)


def new_msg_from_db(pattern):
    """Convert PicTextMsg from db to PicTextMsg object for rendering"""
    items = []

    for item in pattern.handler.all():
        items.append(PTItem(item.title, item.description, item.pic_url, item.url))

    return items


def db_router(recv_msg, *args):
    # 文本类型
    if recv_msg.msg_type == 'text':
        for pattern in PatternT2T.objects.all():
            match = re.search(pattern.content.encode('utf-8'), recv_msg.content)

            if match:
                return text_response(recv_msg, pattern.handler.content)

        for pattern in PatternT2PT.objects.all():
            match = re.search(pattern.content.encode('utf-8'), recv_msg.content)

            if match:
                return pic_text_response(recv_msg, new_msg_from_db(pattern))

    # 事件类型
    if recv_msg.msg_type == 'event':
        for pattern in PatternE2T.objects.all():
            if pattern.event == recv_msg.event:
                if recv_msg.event_key:
                    match = re.search(pattern.event_key.encode('utf-8'), recv_msg.event_key)
                    if match:
                        return text_response(recv_msg, pattern.handler.content)
                else:
                    return text_response(recv_msg, pattern.handler.content)

        for pattern in PatternE2PT.objects.all():
            if pattern.event == recv_msg.event:
                if recv_msg.event_key:
                    match = re.search(pattern.event_key.encode('utf-8'), recv_msg.event_key)
                    if match:
                        return pic_text_response(recv_msg, new_msg_from_db(pattern))
                else:
                    return pic_text_response(recv_msg, new_msg_from_db(pattern))
