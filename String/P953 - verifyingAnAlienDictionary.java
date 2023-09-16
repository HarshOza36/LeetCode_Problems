class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        Map<Character, Integer> orderMap = new HashMap();
        int idx = 0;
        for(char ch: order.toCharArray()){
            orderMap.put(ch, idx++);
        }

        for(int i = 1; i < words.length; i++){
            String w1 = words[i-1], w2 = words[i];

            for(int j = 0; j < w1.length(); j++){
                if(j == w2.length()) return false; // because w2 is prefix of w1, which is not sorted.

                if(w1.charAt(j) != w2.charAt(j)){
                    if(orderMap.get(w2.charAt(j)) < orderMap.get(w1.charAt(j))) return false;
                    // if first different character is valid then they are sorted so break
                    break;
                }
            }   
        }

        return true;
    }
}