import java.util.*;

class Solution {
    
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> map = new HashMap<>();
        for (String mem : participant) {
            map.put(mem, map.getOrDefault(mem, 0) + 1);
        }
        
        for (String mem : completion) {
            if (map.containsKey(mem)) {
                map.put(mem, map.get(mem) - 1);
            }
        }
        
        String answer = "";
        for (String mem : map.keySet()) {
            if (map.get(mem) > 0) {
                answer = mem;
                break;
            }
        }
        
        return answer;
    }
}