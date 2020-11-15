from math import ceil


def who_would_win(mon1, mon2):
    mon1['allhit'] = mon1['hitpoints'] * mon1['number']
    mon2['allhit'] = mon2['hitpoints'] * mon2['number']
    while True:
        mon2['allhit'] = mon2['allhit'] - mon1['number'] * mon1['damage']
        mon2['number'] = ceil(mon2['allhit'] / mon2['hitpoints'])
        if not mon2['number'] > 0: return f"{mon1['number']} {mon1['type']}(s) won"
        mon1['allhit'] = mon1['allhit'] - mon2['number'] * mon2['damage']
        mon1['number'] = ceil(mon1['allhit'] / mon1['hitpoints'])
        if not mon1['number'] > 0: return f"{mon2['number']} {mon2['type']}(s) won"
