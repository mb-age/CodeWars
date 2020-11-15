from itertools import groupby


def trump_detector(speech):
    vowels = 'aeiou'
    letters = [list(j) for i,j in groupby(speech.lower())]
    total = [i for i in letters if i[0] in vowels]
    return round(sum(len(i)-1 for i in total if len(i)>1)/len(total),2)
