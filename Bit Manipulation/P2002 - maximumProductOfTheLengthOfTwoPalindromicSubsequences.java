class Solution {
    public int maxProduct(String s) {
        // We will create a bitmask of size 2^n-1 and then for each i iterating over this mask,
        // we will iterate over the full string and try to form palindromes. If it is a palindrome,
        // we will save it in a hashmap and continue till this 2^n * n loop is completed.
        // Once completed, we will now compare all the keys in the hashmap with all other keys, and
        // apply bitwise & on it. If the result is 0, that means, the characters dont overlap, and we can
        // multiply those palindromes. for example in leetcodecom for ete our mask will be 01010001000 and
        // for cdc our mask will be 00001010100. If we take & of these we will get 0 hence they have no 
        // overlapping charaters.


        Map<Integer, Integer> map = new HashMap();
        // Map will contain key as the bitmask and value as the length of palindrome string
        int maskLength = 1 << s.length();
        for(int mask = 1; mask < maskLength; mask++){
            StringBuilder subseq = new StringBuilder();
            for(int i = 0; i < s.length(); i++){
                if((mask & (1 << i)) > 0){
                    
                    subseq.append(s.charAt(s.length()-1-i));
                }
            }
            String finalString = subseq.toString();
            if(isPalindrome(0, finalString.length()-1, finalString) == true){
                map.put(mask, finalString.length());
            }
        }
        int res = 0;
        for(Integer i : map.keySet()){
            for(Integer j: map.keySet()){
                if((i&j) == 0) res = Math.max(res, map.get(i) * map.get(j));
            }
        }
        return res;
    }
    public boolean isPalindrome(int i, int j, String s){
        if (i >= j) return true;
        if (s.charAt(i) != s.charAt(j)) return false;
        return isPalindrome(i + 1, j - 1, s);
    }
}