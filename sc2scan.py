#!/usr/bin/env python
# -*- coding: utf-8 -*-
army_units = ['Marine',
              'Marauder',
              'Reaper',
              'Ghost',
              'BattleHellion',
              'Hellion',
              'Hellbat',
              'WidowMine',
              'SiegeTank',
              'Cyclone',
              'Thor',
              'Viking',
              'VikingFighter',
              'VikingAssault',
              'Medivac',
              'Liberator',
              'Raven',
              'Banshee',
              'Battlecruiser',
              'Nuke',  # I guess
              'Zealot',
              'Stalker',
              'Sentry',
              'Adept',
              'MothershipCore',
              'HighTemplar',
              'DarkTemplar',
              'Immortal',
              'Disruptor',
              'Colossus',
              'Archon',
              'Observer',
              'WarpPrism',
              'Phoenix',
              'VoidRay',
              'Oracle',
              'Tempest',
              'Carrier',
              'Zergling',
              'Roach',
              'Hydralisk',
              'SwarmHost',
              'Infestor',
              'Ultralisk',
              'Mutalisk',
              'Corruptor',
              'Viper',
              'Baneling',
              'BroodLord',
              'Overseer', ]


def populate_build_data(player, debug):
    data = {}
    if debug and False:
        for event in player['buildOrder']:
            if not event['is_worker']:
                # from pdb import set_trace; set_trace()
                print('debug: {} {} {}{}'.format(
                    event['supply'],
                    event['time'],
                    event['name'],
                    ' (Chronoboosted)' if event['is_chronoboosted'] else ''
                ))

    data.update(first_army_unit(player, debug))

    return data


def first_army_unit(player, debug):
    data = {}
    for event in player['buildOrder']:
        if not event['is_worker']:
            if event['name'] in army_units:
                if debug:
                    print "debug: First army unit found", event['name']
                data['first_army_unit'] = event['name']
                data['first_army_unit_supply'] = str(event['supply'])
                data['first_army_unit_time'] = event['time']
                break
    return data


def map_process(map, debug):
    map = unkorean_maps(map, debug)
    splits = map.split(" ")
    if "LE" in splits:
        splits.remove("LE")
    if "TE" in splits:
        splits.remove("TE")
    if "(Void)" in splits:
        splits.remove("(Void)")

    return " ".join(splits)


# References
# http://sc2.blizzard.cn/articles/1001/76078
# http://tw.battle.net/sc2/zh/blog/20372511/2016-%E7%AC%AC-6-%E8%B3%BD%E5%AD%A3%E5%85%A8%E6%96%B0%E5%A4%A9%E6%A2%AF%E5%9C%B0%E5%9C%96-2016-11-17
def unkorean_maps(map, debug):
    # from pdb import set_trace; set_trace()
    if debug:
        print "map", map
    if u'回聲 - 天梯版' in map:
        return 'Echo'
    if u'密林濕地 - 天梯版' in map:
        return 'Overgrowth'
    if u'旋風之境 - 天梯版' in map:
        return 'Whirlwind'
    if u'紐科克管轄區 - 聯賽版' in map:
        return 'Newkirk Precinct'
    if u'新柯尔克辖区-锦标赛版' in map:
        return 'Newkirk Precinct'
    if u'殖民站 - 天梯版' in map:
        return 'Habitation Station'
    if u'瓦尼研究站' in map:
        return 'Vaani Research Station'
    if u'破曉黎明 - 天梯版' in map:
        return 'Daybreak'
    if debug:
        print "No match"
    return map


def is_korean_map(map):
    korean = True
    for vowel in ['a', 'e', 'i', 'o', 'u']:
        if vowel in map:
            korean = False

    return korean
