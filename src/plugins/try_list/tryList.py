import re

from nonebot import on_fullmatch, on_regex
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Message, MessageSegment

from src.Util.Content import getQQInfoJSONPath
from src.Util.JsonMapper import JsonMapper

tryList = on_regex(pattern=r'^\n下次试试(?!什么)')

catList = on_fullmatch("\n下次试试什么")


@tryList.handle()
async def tryList_handle(event: GroupMessageEvent):
    val = re.sub(r'^\n下次试试', '', event.get_message().__str__())
    result = "\n已将 " + val + " 添加至你的愿望单中"
    mapper = JsonMapper(getQQInfoJSONPath(event.user_id))
    mapper.load()
    _list = mapper.get_value("tryList")
    if _list is "":
        _list = val
    else:
        _list = _list + ',' + val
    mapper.set_value("tryList", _list)
    mapper.save()
    await tryList.finish(MessageSegment.reply(event.message_id) + result)


@catList.handle()
async def catList_handle(event: GroupMessageEvent):
    result = "\n你的愿望单如下：\n"
    mapper = JsonMapper(getQQInfoJSONPath(event.user_id))
    print(getQQInfoJSONPath(event.user_id))
    mapper.load()
    v = mapper.get_value("tryList")
    _v = v.split(",")
    __v = ""
    a = 0
    for i in _v:
        a = a + 1
        __v += "\n" + a.__str__() + "." + i
    await catList.finish(MessageSegment.reply(event.message_id) + result + __v)
