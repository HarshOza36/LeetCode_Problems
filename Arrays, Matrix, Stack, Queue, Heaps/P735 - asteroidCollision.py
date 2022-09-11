class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for new in asteroids:
            while stack and new < 0 < stack[-1]:
                top = stack[-1]
                if top < -new:
                    stack.pop()
                    continue
                elif top == -new:
                    stack.pop()
                break
            else:
                stack.append(new)
            
        return stack