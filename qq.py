import time
from qqbot import QQBotSlot as qqbotslot, RunBot
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

qq_account = config['qq']
group_info = config['group']



def send_timed_message(bot, group_id, content, hour, minute):
    # 发送定时消息的函数
    current_time = time.localtime()
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min

    if current_hour == hour and current_minute == minute:
        bot.SendTo(contact=group_id, content=content)


if __name__ == '__main__':
    # 在这里配置您的 QQ 账号信息
    bot = RunBot()
    group_id = group_info['GroupID']
    content = group_info['Message']
    send_timed_message(bot, group_id, content, 13, 33)