#!/usr/bin/env python

import urllib.request as web
import re
from collections import defaultdict


def read_websites():
    with open("websites") as file_websites:
        return file_websites.readlines()


def main():
    championmasterylookup = defaultdict(int)
    websites = read_websites()
    for counter in range(0, len(websites)):
        with web.urlopen(websites[counter]) as fetch:
            data = fetch.read().decode('UTF-8')
        heroes = re.findall('<a href=\"/champion\?champion=[0-9]+\">(.*)</a>', data)
        mastery_points = re.findall('<td>[0-9]+</td>\n\s+<td data-format-number=\"([0-9]+)\" data-value=', data)
        print(len(heroes), ":", len(mastery_points))
        if len(heroes) != len(mastery_points):
            print("Length mismatch")
            break
        hero_points_tuple = zip(heroes, mastery_points)
        for hero_point_entry in hero_points_tuple:
            championmasterylookup[hero_point_entry[0]] += int(hero_point_entry[1])

    for champion, points in sorted(championmasterylookup.items(), key=lambda x: -x[1]):
        print(champion + ":", points)

if __name__=="__main__":
    main()