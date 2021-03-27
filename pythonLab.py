import sqlite3
import os.path


def exec_script(cursor, path):
    file = open(path, "r")
    script = file.read()
    file.close()
    cursor.execute(script)


def print_longest_film(cursor):
    exec_script(cursor, "getLongestFilm.sql")
    data = cursor.fetchall()[0]
    print("Самый продолжительный фильм", data[2], data[9], sep="\n")


def print_longest_show(cursor):
    exec_script(cursor, "getLongestTVShow.sql")
    data = cursor.fetchall()[0]
    print("Самый продолжительный сериал", data[2], data[9], sep="\n")


def print_most_frequent_pair(cursor):
    actors = {}
    max_freq = 0
    max_pair = []
    cursor.execute("SELECT netflix_titles.cast FROM netflix_titles")
    for data in cursor:
        cast = data[0].split(', ')
        if cast[0] == '':
            continue
        for actor in cast:
            if actor not in actors:
                actors[actor] = {}
            for other in cast:
                if other == actor:
                    continue
                if other not in actors[actor]:
                    actors[actor][other] = 0
                actors[actor][other] += 1
                if actors[actor][other] > max_freq:
                    max_freq = actors[actor][other]
                    max_pair = [actor, other]
    print("Самая частая пара")
    print(max_pair[0], "и", max_pair[1])
    print(max_freq, "раз")


def print_most_frequent_actor(cursor):
    actors = {}
    max_freq = 0
    max_actor = 0
    cursor.execute("SELECT netflix_titles.cast FROM netflix_titles")
    for data in cursor:
        cast = data[0].split(', ')
        if cast[0] == '':
            continue
        for actor in cast:
            if actor not in actors:
                actors[actor] = 0
            actors[actor] += 1
            if actors[actor] > max_freq:
                max_freq = actors[actor]
                max_actor = actor
    print("Самый популярный актер")
    print(max_actor)
    print(max_freq, "раз")


def main():
    if not os.path.exists('netflix.sqlite'):
        print("Отсутствует netflix.sqlite")
        exit(0)
    conn = sqlite3.connect("netflix.sqlite")
    cursor = conn.cursor()
    print_longest_film(cursor)
    print()
    print_longest_show(cursor)
    print()
    print_most_frequent_pair(cursor)
    print()
    print_most_frequent_actor(cursor)


main()
