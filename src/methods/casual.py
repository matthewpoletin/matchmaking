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


def casual(base: Base):
	"""
	Casually (randomly) matches players
	{roomId: room, ...}
	:return:
	"""
	# TODO: get from pool, not base
	unmatched = dict(base.players)
	rooms = {}
	while len(unmatched) > 1:
		p1 = pop_random(unmatched)
		p2 = pop_random(unmatched)
		room = Room([p1, p2])
		base.set_status(p1.uuid, PlayerStatus.PLAYING)
		base.set_status(p2.uuid, PlayerStatus.PLAYING)
		logging.info('Created new room')
		rooms[room.id] = room
		del room
	return rooms
