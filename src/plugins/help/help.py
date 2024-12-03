from nonebot import on_fullmatch, on_keyword
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, Message

bot_time = on_fullmatch('\nhelp')

word = on_keyword({"\n你是谁"})


@word.handle()
async def _(bot: Bot):
    await word.finish(str(bot.self_id))


@bot_time.handle()
async def time_handle(event: GroupMessageEvent):
    rspStr = ("\n牙牙bot，指令均使用\\n前缀触发。可用指令有："
              "\n - help【该消息】"
              "\n - 几点了【发送当前时间】"
              "\n - 下次试试[] & 下次试试什么 【查看和添加愿望单】")
    await bot_time.finish(Message(f"[CQ:at,qq={event.user_id}]") + rspStr)
