import java.util.*;
import java.io.*;

class Solution {
    public int solution(String s) {
        HashMap<Character, Character> map = new HashMap<>(){{
            put(']', '[');
            put(')', '(');
            put('}', '{');
        }};

        ArrayDeque<Character> queue = new ArrayDeque<>();
        for (int i = 0; i < s.length(); i++) {
            queue.addLast(s.charAt(i));
        }

        int answer = 0;
        for (int i = 0; i < s.length(); i++) {
            queue.addLast(queue.pollFirst());
            Stack<Character> st = new Stack<>();
            for (Character ch : queue) {
                if (st.isEmpty()) {
                    st.push(ch);
                    continue;
                }

                if (map.containsKey(ch) && st.peek() == map.get(ch)) {
                    st.pop();
                } else {
                    st.push(ch);
                }
            }

            if (st.isEmpty()) {
                answer++;
            }
        }
        return answer;
    }
}