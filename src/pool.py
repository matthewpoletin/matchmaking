#!/usr/bin/env python3
# -*- coding: utf-8 -*

import uuid


class Pool:
    """
    Class for list of all online players
    """

    # List of all players waiting (UUIDs)
    players = []

    def __init__(self):
        pass

    def add_player(self, player_id: uuid.UUID):
        pass

    def rem_player(self, player_id: uuid.UUID):
        pass

    def get_rand_player(self):
        pass
