def maze_runner(maze, directions):
    def temp(a, b):
        if not 0 <= a < len(maze) or not 0 <= b < len(maze) or maze[a][b] == 1:
            return 'Dead'
        elif maze[a][b] == 3:
            return 'Finish'
    for i in range(len(maze)):
        if 2 in maze[i]:
            a = i
            b = maze[i].index(2)
            break
    for j in directions:
        if j == 'N':
            a -= 1
            temp(a,b)
            if temp(a,b):
                return temp(a,b)
        elif j == 'S':
            a += 1
            temp(a,b)
            if temp(a,b):
                return temp(a,b)
        elif j == 'W':
            b -= 1
            temp(a,b)
            if temp(a,b):
                return temp(a,b)
        elif j == 'E':
            b += 1
            temp(a,b)
            if temp(a,b):
                return temp(a,b)
    return 'Lost'
