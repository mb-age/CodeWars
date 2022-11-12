def fight(r1, r2, t):
    if r1["speed"] < r2["speed"]: r1, r2 = r2, r1
    for i in __import__('itertools').zip_longest(r1['tactics'], r2['tactics']):
        r2['health'] -= t[i[0]]
        if not r2['health']: break
        if i[1]: r1['health'] -= t[i[1]]
    return f"{(r1, r2)[r2['health'] > r1['health']]['name']} has won the fight." if r2['health'] != r1['health'] else 'The fight was a draw.'