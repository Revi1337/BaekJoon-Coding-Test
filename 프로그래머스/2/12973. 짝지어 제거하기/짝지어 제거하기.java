import java.util.*;
import java.io.*;

class Solution
{
        public int solution(String s) {
        Stack<Character> st = new Stack<>();
        for (int i = s.length() - 1; i > -1; i--) {
            if (st.isEmpty()) {
                st.push(s.charAt(i));
                continue;
            }

            if (st.peek() == s.charAt(i)) {
                st.pop();
            } else {
                st.push(s.charAt(i));
            }
        }

        return st.isEmpty() ? 1 : 0;
    }
}