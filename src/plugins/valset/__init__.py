from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata
from .setVal import *
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="valSet",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)

