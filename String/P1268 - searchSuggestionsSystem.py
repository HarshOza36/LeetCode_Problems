class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        products.sort()
        n = len(products)
        l = 0
        r = n - 1
        # TC O(nlogn) + nw + m where n is len of product array
        # w is max length of words and m is len of search word
        for i in range(len(searchWord)):
            ch = searchWord[i]
            # while left <= right and (if product doesnt have ith ch or ith ch of 
            # product at right != current ch)
            
            while l <= r and (len(products[l]) <= i or products[l][i] != ch):
                l += 1      
            # while left <= right and (if product doesnt have ith ch or ith ch of 
            # product at right != current ch)
            while l <= r and (len(products[r]) <= i or products[r][i] != ch):
                r -= 1
                
            # Now we will know that the products in range left and right are valid
            # so they have matching prefix
            ans.append([])
            
            noOfWordsMatching = r - l + 1
            
            for j in range(min(3, noOfWordsMatching)):
                ans[-1].append(products[l + j])
        return ans