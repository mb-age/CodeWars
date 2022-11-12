from itertools import permutations as p

def permutations(s):
    return {''.join(i) for i in p(s)}