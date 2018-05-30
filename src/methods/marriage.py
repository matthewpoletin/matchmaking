#!/usr/bin/env python3
# -*- coding: utf-8 -*


def marriage(players: []):
	"""

	:param players:
	:return:
	"""
	pass


def examine(players: []):
	"""
	:param players:
	:return:
	"""
	diffs = []
	for player_a in players:
		for player_b in players:
			diff = abs(player_a.skill - player_b.skill) / min(player_a.skill, player_b.skill) * 100


def offer(player_a, player_b):
	"""

	:param player_a:
	:param player_b:
	:return:
	"""
	print("match")