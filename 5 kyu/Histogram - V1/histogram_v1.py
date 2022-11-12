from typing import List
def histogram(rolls: List[int]) -> str:
    levels_list = []
    level1 = '1 2 3 4 5 6\n'
    level2 = '-----------\n'
    levels_number = max(rolls)+1
    level_n = ''
    rolls_temp = rolls[:]
    for _ in range(levels_number):
        for index,_ in enumerate(rolls):
            if rolls_temp[index]:
                level_n += '# '
                rolls_temp[index] -= 1
            else:
                level_n += '  '
        levels_list.append(level_n)
        level_n = ''
    for level_index,level in enumerate(levels_list):
        while level_index < len(levels_list)-1:
            if level.count('#') != levels_list[level_index+1].count('#'):
                lev_now = level[::2]
                lev_next = levels_list[level_index+1][::2]
                for index,sign in enumerate(lev_now):
                    if sign == '#' and lev_next[index]==' ':
                        new_str = levels_list[level_index+1][:index*2] + str(rolls[index]).ljust(2) + levels_list[level_index+1][2*index+2:]
                        levels_list[level_index + 1] = new_str
            break
    levels_list.insert(0,level2)
    levels_list.insert(0,level1)
    levels_list = list(map(lambda x:x.rstrip()+'\n',levels_list))
    res=''.join(reversed(levels_list))
    return res