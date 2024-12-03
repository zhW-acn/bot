import re

from nonebot.adapters.onebot.v11 import GroupMessageEvent, Message, Bot, Event
from nonebot import on_message, on_startswith, on_keyword, on_regex

from src.Util.Content import getQQInfoJSONPath
from src.Util.JsonMapper import JsonMapper

getVal = on_regex(pattern=r'^\nget\s+([^\s]+)$')


@getVal.handle()
async def get_handle(event: GroupMessageEvent):

    print(event.user_id)
    await getVal.finish(Message(f"[CQ:at,qq={event.user_id}]") + event.get_message())
    # match = re.match(pattern, event.get_message().__str__(), re.IGNORECASE)  # 忽略大小写
    # if match:
    #     k = match.group(1)
    #     mapper = JsonMapper(getQQInfoJSONPath(event.user_id))
    #     mapper.load()
    #     v = mapper.get_value(k)
    #     if v is "":
    #         await getVal.finish(Message(f"[CQ:at,qq={event.user_id}]") + "没有 " + k + " 这样的值喔")
    #     else:
    #         await getVal.finish(Message(f"[CQ:at,qq={event.user_id}]") + v)
    # else:
    #     await getVal.finish(Message(f"[CQ:at,qq={event.user_id}]") + "输入格式错误")
