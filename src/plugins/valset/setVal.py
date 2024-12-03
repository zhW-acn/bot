import re

from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.adapters.onebot.v11 import Message
from nonebot.plugin.on import on_fullmatch

from src.Util.Content import getQQInfoJSONPath
from src.Util.JsonMapper import JsonMapper

setVal = on_fullmatch({'set'})


@setVal.handle()
async def test_handle(event: GroupMessageEvent):
    pattern = r"^/set\s+([^\s]+)\s+([^\s]+)$"
    print(event.get_message().__str__())
    match = re.match(pattern, event.get_message().__str__(), re.IGNORECASE)  # 忽略大小写
    if match:
        k = match.group(1)
        v = match.group(2)
        mapper = JsonMapper(getQQInfoJSONPath(event.user_id))
        mapper.load()
        mapper.set_value(k, v)
        mapper.save()
        await setVal.finish(Message(f"[CQ:at,qq={event.user_id}]") + "设置成功")
    else:
        await setVal.finish(Message(f"[CQ:at,qq={event.user_id}]") + "输入格式错误")