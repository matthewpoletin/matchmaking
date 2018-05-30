#!/usr/bin/env python3
# -*- coding: utf-8 -*

import random
import logging
import uuid

from src.base import Base, PlayerStatus
from src.room import Room


def pop_random(players):
    """
    Pops random player from dictionary
    :param players:
    :return:
    """
    if len(list(players.keys())) != 0:
        player_id = list(players.keys())[random.randint(0, len(list(players.keys()))) - 1]
        return (players.pop(player_id))[0]
    else:
        return None


def find_closest(skill, players):
    """
    Находит игрока с ближайшим опытом
    :param skill: Опыт игрока
    :param players:
    :return:
    """
    closest = players[list(players.keys())[0]]
    for player_id, player in players.items():
        if abs(skill - closest[0].skill) > abs(skill - player[0].skill):
            closest = player
    return players.pop(closest[0].uuid)[0]


def experience(base: Base):
    """
    Соединяет игроков в пары на основании опыта
    {roomId: room, ...}
    :param base: База доступных игроков
    :return:
    """
    # TODO: get from pool, not base
    unmatched = dict(base.players)
    rooms = {}
    while len(unmatched) > 1:
        p1 = pop_random(unmatched)
        p2 = find_closest(p1.skill, unmatched)
        room = Room([p1, p2])
        base.set_status(p1.uuid, PlayerStatus.PLAYING)
        base.set_status(p2.uuid, PlayerStatus.PLAYING)
        logging.info('Created new room')
        rooms[room.id] = room
        del room
    return rooms
