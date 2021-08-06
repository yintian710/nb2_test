import nonebot
from nonebot.adapters.cqhttp import Bot as CQHTTPBot

nonebot.init()
driver = nonebot.get_driver()
driver.register_adapter("cqhttp", CQHTTPBot)
nonebot.load_plugins('awesome/plugins')
nonebot.load_plugin("nonebot_plugin_test")
nonebot.load_builtin_plugins()

if __name__ == "__main__":
    nonebot.run()
