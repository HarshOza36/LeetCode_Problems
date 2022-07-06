class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if(image[sr][sc] == color):
            return image
        
        def floodFillHelper(image, sr, sc, old_color, new_color):    
            if(sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0])):
                return
            color = image[sr][sc]
            
            if(color == old_color):
                image[sr][sc] = new_color
                floodFillHelper(image, sr - 1, sc, old_color, new_color)
                floodFillHelper(image, sr, sc - 1, old_color, new_color)
                floodFillHelper(image, sr + 1, sc, old_color, new_color)
                floodFillHelper(image, sr, sc + 1, old_color, new_color)
        floodFillHelper(image, sr, sc, image[sr][sc], color)
        return image