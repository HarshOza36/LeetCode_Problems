class Solution {
    public int countVowelSubstrings(String word) {
        // Bruteforce can work on 100 chars by checking all substrings in O(n^2) and using one set which
        // keeps track of all vowels seen.
        // O(n) approach can be using a sliding window with a hashmap
        HashMap<Character,Integer> map = new HashMap();
        map.put('a', 0);
        map.put('e', 0);
        map.put('i', 0);
        map.put('o', 0);
        map.put('u', 0);
        int ans = 0, l = 0, r = 0, seenVow = 0;
        for (int i = 0; i < word.length(); i++){
            char ch = word.charAt(i);
            if(map.get(ch) != null){
                map.put(ch, map.get(ch)+1);
                if(map.get(ch) == 1) seenVow++;

                while(seenVow == 5){
                    char chAtR = word.charAt(r);
                    map.put(chAtR, map.get(chAtR) - 1);
                    if(map.get(chAtR) == 0) seenVow--;
                    r++;
                }
                ans = ans + (r-l);

            }else{
                map.forEach((k,v)->map.put(k, 0));
                seenVow = 0;
                l = r = i+1;
            }
        }
        return ans;
    }
}