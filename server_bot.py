import time,requests
# from typing import Optional
from abc import ABCMeta, abstractmethod

class INotifier(metaclass=ABCMeta):
    @property
    @abstractmethod
    def PLATFORM_NAME(self) -> str:
        """
        将 PLATFORM_NAME 设为类的 Class Variable，内容是通知平台的名字（用于打日志）。
        如：PLATFORM_NAME = 'Telegram 机器人'
        :return: 通知平台名
        """
    @abstractmethod
    def notify(self, *, success, msg, data,username, name) -> None:
        """
        通过该平台通知用户操作成功的消息。失败时将抛出各种异常。
        :param success: 表示是否成功
        :param msg: 成功时表示服务器的返回值，失败时表示失败原因；None 表示没有上述内容
        :return: None
        """

TIMEOUT_SECOND = 25

class ServerJiangNotifier(INotifier):
    PLATFORM_NAME = 'Server 酱'

    def __init__(self, *, sckey: str, sess: requests.Session):
        self._sckey = sckey
        self._sess = sess

    def notify(self, *, success, msg, data, username, name) -> None:
        title_str,body_str='',''
        
        # 调用 Server 酱接口发送消息
        sc_res_raw = self._sess.post(
            f'https://sctapi.ftqq.com/{self._sckey}.send',
            data={
                'title': f'{title_str}',
                'desp': f'{body_str}',
            },
            timeout=TIMEOUT_SECOND,
        )
