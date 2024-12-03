from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata
from .getVal import *
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="valGet",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)

