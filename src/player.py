# -*- coding: utf-8 -*

import random
import uuid

maxAllowedAge = 18
minAge = maxAllowedAge
maxAge = 100
minArmLength = 1
maxArmLength = 100
minHeight = 140
maxHeight = 300
minExperience = 0
maxExperience = maxAge - maxAllowedAge
minGamesPlayed = 0
maxGamesPlayed = 100
minSkill = 100
maxSkill = 5000
minWR = 35
maxWR = 65
minPause = 0
maxPause = 28


class Player:
    def __init__(self):
        self.uuid = None
        self.skill = None
        self.wr = None
        self.pause = None
        # self.age = None
        # self.height = None
        # self.gamesPlayed = None
        # self.experience = None

    @staticmethod
    def generate():
        player = Player()
        player.uuid = uuid.uuid4()
        player.skill = random.randint(minSkill, maxSkill)
        player.wr = random.randint(minWR, maxWR)
        # player.age = random.randint(minAge, maxAge)
        # player.height = random.randint(minHeight, maxHeight)
        # player.gamesPlayed = random.randint(minGamesPlayed, maxGamesPlayed)
        # player.experience = random.randint(minExperience, maxExperience)
        player.pause = random.randint(minPause, maxPause)
        return player

    def __str__(self):
        print('\n' + '\033[1;34m' + 'Player Info:' + '\033[0m')
        print('player: ' + str(self.uuid))
        print('skill: ' + str(self.skill))
        print('wr: {}%'.format(self.wr))
        # print('age: ' + str(self.age) + 'y.o.')
        # print('height: ' + str(self.height) + 'cm')
        # print('gamesPlayed: ' + str(self.gamesPlayed))
        # print('experience: ' + str(self.experience) + ' years')
        return ""
