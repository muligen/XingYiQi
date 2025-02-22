# -*- coding: utf-8 -*-
"""
游戏全局规则，对应菜单栏
@Time    : 2023/10/6 16:03
@Author  : wenjiawei
"""
from collections import OrderedDict

from QiPan import QiPan
from QiZi import Soldier, King
from Serializable import Serializable


class Game(Serializable):

    def __init__(self):
        super().__init__()
        self.pan = None

    def start(self, msg=None):
        print(f"游戏开始 {msg}")

        # 初始化棋盘
        pan = QiPan(self)
        self.pan = pan

        # 初始化双方棋子
        King(pan, (0, 2), False)
        Soldier(pan, (0, 0), False)
        Soldier(pan, (0, 1), False)
        Soldier(pan, (0, 3), False)
        Soldier(pan, (0, 4), False)

        King(pan, (4, 2), True)
        Soldier(pan, (4, 0), True)
        Soldier(pan, (4, 1), True)
        Soldier(pan, (4, 3), True)
        Soldier(pan, (4, 4), True)

        # 返回给客户端
        return self.serialize()

    def pause(self, msg=None):
        print(f"游戏暂停 {msg}")

    def over(self, msg=None):
        print(f"游戏结束 {msg}")

    def serialize(self):
        return OrderedDict([
            ('id', self.id),
            ("game_id", self.id),
            ("pan", self.pan.serialize()),
        ])
