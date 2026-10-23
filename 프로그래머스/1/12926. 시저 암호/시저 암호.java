class Solution {
    
    public String solution(String string, int n) {
        StringBuilder sb = new StringBuilder();
        for (char ch : string.toCharArray()) {
            if (Character.isUpperCase(ch)) {
                sb.append((char) ('A' + (ch - 'A' + n) % 26));
            } else if (Character.isLowerCase(ch)) {
                sb.append((char) ('a' + (ch - 'a' + n) % 26));
            } else {
                sb.append(ch);
            }
        }
        return sb.toString();
    }
}