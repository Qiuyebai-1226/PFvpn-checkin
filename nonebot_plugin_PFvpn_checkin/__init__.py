import os
import nonebot
from nonebot import on_command
import nonebot_plugin_apscheduler
from nonebot.adapters.onebot.v11 import Bot, MessageSegment, PrivateMessageEvent
from pathlib import Path
from nonebot import logger


__plugin_meta__ = nonebot.plugin.PluginMetadata(
    name='PFvpn自动签到',
    description='用于PFvpn的全自动签到，并将签到结果发送给superuser！',
    usage='''每日自动执行''',
    extra={'version': '1.14.514'}
)

#此处修改自动签到时间
@nonebot_plugin_apscheduler.scheduler.scheduled_job("cron", hour='15', minute='50', id="PFvpn")
async def _3():
    os.system("python checkin.py")
    bot = nonebot.get_bot()
    p = Path(__file__).absolute().parents[3] 

    # 这里改成自己的qq号
    await bot.send_private_msg(user_id=114514, message=MessageSegment.image(p/'result.png'))

handel_checkin = on_command("vpn签到",aliases={"checkin"},priority=5,block=True)
@handel_checkin.handle()
async def _checkin(bot:Bot,event:PrivateMessageEvent):
    os.system("python checkin.py")
    p = Path(__file__).absolute().parents[3] 
    logger.info(p)
    await handel_checkin.finish(MessageSegment.image(p/'result.png'))

# os.system("python checkin.py")