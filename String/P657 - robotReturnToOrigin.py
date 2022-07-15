class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if(len(moves) & 1 == 1):
            return False # if there are odd number of moves you cant reach back
        x,y = 0,0
        for move in moves:
            if move == "R": y += 1
            elif move == "L": y -= 1
            elif move == "U": x -= 1
            elif move == "D": x += 1
        return x == 0 and y == 0
                