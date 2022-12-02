# 캐릭터의 좌표

# 가로측 좌표 r과 세로측 좌표 u를 정하고 방향마다 움직임을 정해준다.
def solution(keyinput, board):
    r, u = 0, 0
    for i in keyinput:
        if i == "left":
            r -= 1
        elif i == "right":
            r += 1
        elif i == "up":
            u += 1
        else:
            u -= 1
# board 값을 통해 좌표의 증가 범위를 제한해준다.
        if r > board[0]//2:
            r = board[0]//2
        elif r < board[0]//2*-1:
            r = board[0]//2*-1
        elif u > board[1]//2:
            u = board[1]//2
        elif u < board[1]//2*-1:
            u = board[1]//2*-1  
    return [r, u]
