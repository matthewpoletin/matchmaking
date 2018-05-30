#!/usr/bin/env python3
# -*- coding: utf-8 -*

import random
import uuid
from enum import Enum, unique

from src.player import Player


@unique
class PlayerStatus(Enum):
    OFFLINE = 1
    SEARCHING = 2
    PLAYING = 3


class Base:
    """
    Class for list of all players in the system
    """

    # {uuid: [player, status], ...}
    players = {}

    def __init__(self, players=None):
        if players is not None:
            self.players = players

    def load_csv(self, file: str):
        """
        Loads list of all players from csv file
        :param file: Absolute path to file location
        :type file: str
        :return:
        """
        raise NotImplementedError

    def load_api(self, t='DEV'):
        """
        Loads list of all players from public api
        :param t: Type of api to use (DEV - local, PROD - remote)
        :return:
        """
        if t == 'DEV':
            return
        elif t == 'PROD':
            pass
            return
        else:
            raise TypeError("t should be 'DEV' or 'PROD'")

    def generate(self, size: int):
        """
        Generates list of all players
        :param size:
        :return:
        """
        if not isinstance(size, int):
            raise TypeError("Type of base size should be int")
        for i in range(size):
            p = Player.generate()
            self.players[p.uuid] = [p, PlayerStatus.OFFLINE]

    def get_player(self, player_id: uuid.UUID):
        """
        Finds player by uuid
        :param player_id:
        :return: Player
        """
        p = self.players.get(player_id)
        return self.players.get(player_id)[0]

    def get_status(self, player_id: uuid.UUID):
        """
        Returns current status of the player
        :param player_id:
        :return:
        """
        return self.players.get(player_id, None)[1]

    def set_status(self, player_id: uuid.UUID, status: PlayerStatus or str):
        """
        Changes status of specified player
        :param player_id:
        :param status:
        :return:
        """
        if type(status) is str:
            status = PlayerStatus(status)
        player = self.get_player(player_id)
        if player is not None:
            self.players[uuid] = [player, status]

    def get_random(self):
        """
        Takes random player of the list
        :return: random player
        :rtype: Player
        """
        # TODO: Add check for an empty list
        return self.players[list(self.players.keys())[random.randint(0, len(list(self.players.keys())) - 1)]][0]

    def __repr__(self):
        for player_id in self.players:
            print(self.players[player_id][0])
            print(self.players[player_id][1])
        return ''
