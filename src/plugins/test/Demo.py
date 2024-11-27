from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Message
from nonebot.internal.matcher import Matcher
from nonebot.internal.params import Arg, ArgPlainText
from nonebot.params import CommandArg

Demo = on_keyword({'weather'})

@Demo.handle()
async def test_handle(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()
    if plain_text:
        matcher.set_arg("city", args)


@Demo.got("city", prompt="你想查询哪个城市的天气呢？")
async def handle_city(city: Message = Arg(), city_name: str = ArgPlainText("city")):
    if city_name not in ["北京", "上海"]:
        city_weather = await Demo.reject(city.template("你想查询的城市 {city} 暂不支持，请重新输入！"))
    city_weather = await get_weather(city_name)
    await Demo.finish(city_weather)


async def get_weather(city: str) -> str:
    return f"{city}今天的天气是晴天."