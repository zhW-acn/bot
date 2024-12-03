from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata

from .config import Config
from .tryList import *

__plugin_meta__ = PluginMetadata(
    name="下次试试什么",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)

