class Solution {
    public boolean checkIfPangram(String sentence) {
        // no letters 
        int seen = 0;
        for(char c:sentence.toCharArray()) {
            // get index of curr char
            int ci = c - 'a';
            // currbit is 1 << ci, OR add curr bit to seen 
            seen = seen | (1<<ci);
        }
        // check if all 26 bits are 1
        return seen == ((1<<26) - 1);
    }
}