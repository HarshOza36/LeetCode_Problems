# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
#        # Brute Force - Accepted
#        # check base case
#         if not root.left and not root.right:
#             return 1
        
#         freq = {}
#         cnt = [0]
#         def dfs(root, pathCount):
#             if root.val not in freq: freq[root.val] = 1
#             else: freq[root.val] += 1
#             if root.left: dfs(root.left, 1+pathCount)
#             if root.right: dfs(root.right, 1+pathCount)
#             # if pathCount is odd, we need all evens and at most one odd
#             # else we need all evens
#             if not root.left and not root.right:
#                 # if we reached the leaf
#                 evens = 0
#                 odds = 0
#                 for v in freq.values():
#                     if v%2 == 0: evens += 1
#                     else: odds += 1
                
#                 # if the whole path is same number its a palindrome
#                 if len(freq) == 1 and list(freq.values())[0] == pathCount:
#                     cnt[0]+= 1
                
                
#                 elif pathCount % 2 == 0:
#                     if odds == 0 and evens != 0: 
#                         cnt[0] += 1
#                 else:
#                     if odds == 1 and evens != 0: 
#                         cnt[0] += 1

#             freq[root.val] -= 1
#             if freq[root.val] == 0: freq.pop(root.val)
#             return
        
#         dfs(root, 1)
#         return cnt[0]

        # faster Bit Manipulation
        def preorder(root, path):
            nonlocal cnt
            if root:
                # compute occurences of each digit 
                # in the corresponding register
                path = path ^ (1 << root.val)
                # if it's a leaf, check if the path is pseudo-palindromic
                if not root.left and not root.right:
                    # check if at most one digit has an odd frequency
                    if path & (path - 1) == 0:
                        cnt += 1
                else:                    
                    preorder(root.left, path)
                    preorder(root.right, path) 
        
        cnt = 0
        preorder(root, 0)
        return cnt