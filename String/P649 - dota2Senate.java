class Solution {
    public String predictPartyVictory(String senate) {
        // At every round, we will check who will win.
        // Winners will be added back to their queue and will be
        // fought with the other queue members.
        // Finally whichever team has more senates win.
        Deque<Integer> qr = new ArrayDeque<>();
        Deque<Integer> qd = new ArrayDeque<>();
        int n = senate.length();
        for(int i = 0; i < n; i++){
            if(senate.charAt(i) == 'R') qr.addLast(i);
            else qd.addLast(i);
        }
        while(!qr.isEmpty() && !qd.isEmpty()){
            int r_i = qr.removeFirst();
            int d_i = qd.removeFirst();
            if(r_i < d_i) qr.addLast(r_i + n);
            else qd.addLast(d_i + n);
        }
        return qr.size() > qd.size() ? "Radiant" : "Dire";
    }
}