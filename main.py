#!/usr/bin/env python3
# -*- coding: utf-8 -*
import sys
import itertools
import random

from src.base import Base
from src.methods.casual import casual
from src.methods.experience import experience
from src.tools.gaussian import gaussian


def predict(rooms):
    """
    Predicts match result
    :param rooms: {roomId: room, ...}
    :return: {roomId: playerId, ...}
    """
    print("Предсказываю результаты матчей")
    prediction = {}  # {roomId: playerId, ...}
    for room_id, room in rooms.items():
        prediction[room_id] = room.predict_winner().uuid
    return prediction


def simulate(rooms):
    """
    Simulates match result
    :param rooms: {roomId: room, ...}
    :return: {roomId: playerId, ...}
    """
    print("Моделирую результаты матчей")
    model = {}  # {roomId: playerId, ...}
    for room_id, room in rooms.items():
        if len(room.players) > 1:
            room_skill = {}  # {playerId: skill, ...}
            for player in room.players:
                room_skill[player.uuid] = player.skill \
                                          * random.uniform(gaussian(player.pause, 1, 0, 100), 1)\
                                          * random.uniform(1, 1.05)
            winner_id = max(room_skill, key=room_skill.get)
            model[room_id] = winner_id
    return model


def main(argv):
    # Generate bases of players
    base1000 = Base()
    base1000.generate(1000)

    base100 = Base(dict(itertools.islice(base1000.players.items(), 100)))
    base500 = Base(dict(itertools.islice(base1000.players.items(), 500)))
    bases = [base100, base500, base1000]

    methods = {
        'метод на опыте': experience,
        'случайный метод': casual,
    }

    # 	100		500		1000
    # results = [
    #     [0,     0,      0],  # experience
    #     [0,     0,      0],  # casual
    # ]
    results = {}
    for method in methods:
        results[method] = []

    for base_index, base in enumerate(bases):
        print("\nРаботаю с базой в {} игроков".format(len(base.players)))
        for name, method in methods.items():
            print("\nИспользую {}".format(name))
            # Генерируем комнаты случайным методом
            rooms = method(base)
            # Предсказываем результат матча
            prediction = predict(rooms)
            # Моделируем результат матча
            sim = simulate(rooms)
            # Сравниваем предсказание и результат
            print("Сравниваю предсказание и результат")
            shared_items = set(prediction.items()) & set(sim.items())
            quality = round((len(shared_items) / len(prediction) * 100), 2)
            print("Точность результата: {0:.2f}%".format(quality))
            results[name].append(quality)

    print(results)

    # row_format = "{:>15}" * (len(teams_list) + 1)
    # print(row_format.format("", *teams_list))
    # for team, row in zip(teams_list, data):
    #     print(row_format.format(team, *row))

if __name__ == "__main__":
    main(sys.argv)
