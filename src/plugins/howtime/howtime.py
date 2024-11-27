import time

from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Message

bot_time = on_fullmatch('\n几点了')


@bot_time.handle()
async def time_handle(event: GroupMessageEvent):
    localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    await bot_time.finish(Message(f"[CQ:at,qq={event.user_id}]") + localtime)
