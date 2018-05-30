#!/usr/bin/env python3
# -*- coding: utf-8 -*
import logging
import uuid


class Room:
	"""
	Class for a single server
	"""

	# UUID
	id = None
	# List of players
	players = []
	# Maximum size, 0 for infinite
	max_size = 0

	def __init__(self, players: list, max_size=0):
		"""
		Constructor for a room class
		:param max_size: Maximum size
		:param players:
		"""
		self.id = uuid.uuid4()
		self.max_size = max_size
		if not len(players) > max_size:
			logging.error('Size mismatch')
		self.players = players

	def predict_winner(self):
		"""
		For MM predict the winner
		:return: player
		"""
		if len(self.players) > 1:
			# TODO: convert to using of max() function
			winner = self.players[0]
			for player in self.players:
				if player.wr > winner.wr:
					winner = player
			return winner
		else:
			return None

	def add_player(self, player):
		"""
		Adds specified player to the room
		:param player:
		:return:
		"""
		self.players.append(player)

	def remove_player(self, player):
		"""
		Removes specified player from the room
		:param player:
		:return:
		"""
		self.players.remove(player)

	def __repr__(self):
		print('Room {}'.format(self.id))
		print('Players: {}'.format(len(self.players)))
		for player in self.players:
			print(player.uuid)
		return ''
