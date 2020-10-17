def solution(board, moves):
    answer = 0
    pick = []
    screen = []
    for i in range(len(board)):
         screen.append([])

    for row in reversed(board):
 
        for i in range (len(row)):
            if row[i] != 0:
                screen[i].append(row[i])
    

    for move in moves:
        if(len(screen[move - 1])) != 0 :
            if len(pick) == 0:
                 pick.append(screen[move - 1][-1])
            else:
                if pick[-1] != screen[move - 1][-1] :
                    pick.append(screen[move - 1][-1])
                else :
                    pick.pop()
                    answer += 2
            screen[move - 1].pop()
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board,moves))